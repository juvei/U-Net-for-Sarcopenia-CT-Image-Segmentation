import os
#import openpyxl
import matplotlib.pyplot as plt

from torch import nn,optim
import torch
from torch.utils.data import DataLoader
from data import *
from net import *
from torchvision.utils import save_image

#wb = openpyxl.load_workbook('loss.xlsx',data_only=True)
#s1 = wb.create_sheet('loss-epoch')
epoch_loss = []

device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
weight_path='params/unet.pth'
data_path=r'data'
save_path='train_image'
if __name__ == '__main__':
    data_loader=DataLoader(MyDataset(data_path),batch_size=2,shuffle=True)
    net=UNet().to(device)
    if os.path.exists(weight_path):
        net.load_state_dict(torch.load(weight_path))
        print('successful load weight！')
    else:
        print('not successful load weight')

    opt=optim.Adam(net.parameters())
    loss_fun=nn.BCELoss()

    epoch=1
    while epoch<=300:
        running_loss = 0.0
        for i,(image,segment_image) in enumerate(data_loader):
            image, segment_image=image.to(device),segment_image.to(device)

            out_image=net(image)
            train_loss=loss_fun(out_image,segment_image)

            opt.zero_grad()
            train_loss.backward()
            opt.step()

            running_loss += train_loss.item()

            if i%5==0:
                print(f'{epoch}-{i}-train_loss===>>{train_loss.item()}')

            if i%50==0:
                torch.save(net.state_dict(),weight_path)

            _image=image[0]
            _segment_image=segment_image[0]
            _out_image=out_image[0]

            img=torch.stack([_image,_segment_image,_out_image],dim=0)
            save_image(img,f'{save_path}/{i}.png')

        avg_loss = running_loss/100 #training set size
        epoch_loss.append(avg_loss)
        epoch+=1

plt.plot(range(1, 300+1), epoch_loss, label='Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss vs. Epoch')
plt.legend()
plt.savefig('./loss2epoch.jpg')
plt.show()