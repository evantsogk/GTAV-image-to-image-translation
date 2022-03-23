# GTA V Image-to-Image Translation
You can find my thesis in English [here](https://dspace.lib.ntua.gr/xmlui/handle/123456789/54709?locale-attribute=en).

This project aims to transform GTA V images so that they have the style of two different real-world datasets. The image-to-image translation models used for that purpose are [CycleGAN](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix), [AttentionGAN](https://github.com/Ha0Tang/AttentionGAN), [CUT](https://github.com/taesungp/contrastive-unpaired-translation), and [DCLGAN](https://github.com/JunlinHan/DCLGAN). Additionally, the translated results are evaluated using common GAN metrics such as IS, FID, and KID, as well as through the performance in semantic segmentation using DeepLabv3+. The inspiration comes from [CyCADA](https://arxiv.org/pdf/1711.03213.pdf) and [Enhancing photorealism enhancement](http://vladlen.info/papers/EPE.pdf).

Translation example using CycleGAN:
<img src="imgs/cover.png">

Semantic segmentation example of DeepLabv3+ trained with CycleGAN's translated images from GTA V to Cityscapes:
<p float="left">
  <img src="imgs/46_image.png" width="350"/>
  <img src="imgs/46_cyclegan.png" width="350"/> 
</p>

The following is a simple guide to prepare the data and perform image-to-image translation. I use CycleGAN as an example because it produces the best results, but the process is very similar for the other models.


## 1. Download datasets


## 2. Prepare data


## 3. Perform image-to-image translation using CycleGAN
