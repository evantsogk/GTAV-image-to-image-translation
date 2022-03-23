# GTA V Image-to-Image Translation

Master's thesis: Unpaired translation of Grand Theft Auto V images
to real urban scenes using PyTorch.

This project aims to transform GTA V images so that they have the style of two different real-world datasets. The image-to-image translation models used for that purpose are [CycleGAN](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix), [AttentionGAN](https://github.com/Ha0Tang/AttentionGAN), [CUT](https://github.com/taesungp/contrastive-unpaired-translation), and [DCLGAN](https://github.com/JunlinHan/DCLGAN). Additionally, the translated results are evaluated using common GAN metrics such as IS, FID, and KID, as well as through the performance in semantic segmentation using DeepLabv3+. The inspiration comes from [CyCADA](https://arxiv.org/pdf/1711.03213.pdf) and [Enhancing photorealism enhancement](http://vladlen.info/papers/EPE.pdf).

You can find my thesis in English [here](https://dspace.lib.ntua.gr/xmlui/handle/123456789/54709?locale-attribute=en).
