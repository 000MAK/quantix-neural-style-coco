import argparse
from pathlib import Path
import torch
from torch import nn
from torchvision import transforms,models
from PIL import Image

def image(path,size): return transforms.Compose([transforms.Resize(size),transforms.ToTensor()])(Image.open(path).convert('RGB')).unsqueeze(0)
def main():
 p=argparse.ArgumentParser(); p.add_argument('--content',default=''); p.add_argument('--style',default=''); p.add_argument('--steps',type=int,default=100); a=p.parse_args(); r=Path(__file__).parent; (r/'outputs').mkdir(exist_ok=True)
 if not a.content or not a.style: raise SystemExit('Provide --content and --style image paths.')
 device='cuda' if torch.cuda.is_available() else 'cpu'; size=256; content=image(a.content,size).to(device); style=image(a.style,size).to(device); v=models.vgg19(weights=models.VGG19_Weights.DEFAULT).features[:22].eval().to(device)
 for q in v.parameters(): q.requires_grad=False
 layers={3,8,17,21}
 def feats(x):
  result=[]
  for i,layer in enumerate(v):
   x=layer(x)
   if i in layers: result.append(x)
  return result
 with torch.no_grad(): cf=feats(content); sf=feats(style)
 generated=nn.Parameter(content.clone()); opt=torch.optim.Adam([generated],lr=.02)
 for _ in range(a.steps):
  opt.zero_grad(); gf=feats(generated); loss=0
  for c,s,g in zip(cf,sf,gf):
   loss+=torch.nn.functional.mse_loss(g,c)*1e3+torch.nn.functional.mse_loss(g.mean((2,3)),s.mean((2,3)))*1e5
  loss.backward(); opt.step(); generated.data.clamp_(0,1)
 transforms.ToPILImage()(generated.detach().cpu().squeeze()).save(r/'outputs/stylized.png'); print('Saved outputs/stylized.png; final loss',round(float(loss),3))
if __name__=='__main__': main()
