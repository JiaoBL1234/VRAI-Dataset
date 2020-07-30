# VRAI-Dataset
The VRAI Vehicle Re-identification Dataset.

Our VRAI is released now！<br>

Thanks for your interest in our VRAI dataset.<br>

Our VRAI dataset is used for Vehicle Re-identification research in aerial imagery. With the rapid development of the Unmanned Aerial Vehicles (UAVs), the UAV-based vision applications have been drawing an increasing attentions from both industry and academia. However, the UAV-based vehicle reidentiﬁcation is rarely studied, although it has a variety of potential applications such as long-term tracking, visual object retrieval, etc. One of the reasons is the lack of the corresponding publicly available dataset, which will take a large amount of human efforts for UAV ﬂying, video capture and data annotation. In this case, we collect and release our VRAI to support in-depth research.<br>


## Dataset partition:


The VARI dataset is split to the training set and testing set, among which the training set contains 66,113 images with 6,302 IDs, and the test set contains 71,500 images with 6,720 IDs. Besides, we subsample a subset from the testing set as the testing_dev set. The testing_dev set contains 10% images of testing set.<br>

## Annotation:

### Trainng set:
    Image name: ID_Cam_Frame.jpg, such as 0000000X_000Y_0000000Z.jpg, the 0000000X indicates this image belongs to ID No.X, the 000Y indicates this image is captured by camera Y and 0000000z indicates this image is the Z th frame in this trajectory.
    Annotation files: train_annotation.pkl
                      train_im_names: The File Names of images in the training set.
                      color_label: A dictionary to store the mapping from IDs to Vehicle Color Labels.
                      type_label: A dictionary to store the mapping from IDs to Vehicle Type Labels.
                      bumper_label & wheel_label & sky_label & luggage_label: A dictionary to store the mapping from IDs to Vehicle Attributes.
                      d_part_label: A dictionary to store the mapping from Image Names to Vehicle Discriminative Parts Bounding Boxes.
### Testing set:
    Image name: Random_string_Cams.jpg such as 00AV11D2_C1.jpg, the 00AV11D2 is a random string and the C1 indicates this image is captured by camera 1.
    Annotation files: test_annotation.pkl
                      test_im_names: The File Names of images in the testing set.
                      color_label: A dictionary to store the mapping from Image Names to Vehicle Color Labels.
                      type_label: A dictionary to store the mapping from Image Names to Vehicle Type Labels.
                      bumper_label & wheel_label & sky_label & luggage_label: A dictionary to store the mapping from Image Names to Vehicle Attributes. 
                      d_part_label: A dictionary to store the mapping from Image Names to Vehicle Discriminative Parts Bounding Boxes. 
                      gallery_order: A list to store Image Names in gallery set. It also reflects the Index of gallery images. 
                      query_order: A list to store Image Names in query set. It also reflects the Index of query images. 
### Testing_Dev set:
    Image name: Random_string_Cams.jpg, such as 00AV11D2_C1.jpg, the 00AV11D2 is a random string and the C1 indicates image is captured by camera 1.
    Annotation files: test_dev_annotation.pkl
                      dev_im_names: The File Names of images in the Testing_Dev set.
                      color_label: A dictionary to store the mapping from Image Names to Vehicle Color Labels.
                      type_label: A dictionary to store the mapping from Image Names to Vehicle Type Labels.
                      bumper_label & wheel_label & sky_label & luggage_label: A dictionary to store the mapping from Image Names to Vehicle Attributes.
                      d_part_label: A dictionary to store the mapping from Image Names to Vehicle Discriminative Parts Bounding Boxes.
                      gallery_order: A list to store Image Names in gallery set. It also reflects the Index of gallery images.
                      query_order: A list to store Image Names in query set. It also reflects the Index of query images.
The values of color_label are 1, 2, ... , 8 which represent to White, Black, Gray, Red, Green, Blue, Yellow, Brown and Others. The values of type_label are 1, 2, ... , 6 which represent to Sedan, Hatchback, SUV, Bus, Lorry, Truck and Others. The values of bumper_label, and wheel_label, sky_label and luggage_label are 0,1 which represent to whether vehicle instances contain these attributes or not. The distributions of each categories of color and vehicle type is slightly different from the statistical informations in our <a href='https://arxiv.org/pdf/1904.01400.pdf'>paper</a>, since we have cleaned up the annotation again.
             
## Evaluation Metrics:

We adopt the popular mean Average Precision (mAP) and Cumulative Matching Cure (CMC) as in other ReID works. Besides, we host a challenge in Evalai. You can test the performance on our VRAI through this challenge. We also provide an example submission submission_t.json for you.


You can download our VRAI dataset at:


Google Drive:
<a href='https://drive.google.com/drive/folders/1nsxZjrGvO1wfqas_rWTd9TxCeMyLWqMm?usp=sharing'>Google</a>

Baiduyun:
<a href='https://drive.google.com/drive/folders/1nsxZjrGvO1wfqas_rWTd9TxCeMyLWqMm?usp=sharing'>Baiduyun</a>

## Statement:

Our VRAI is prohibited for any commercial using. If you use VRAI dataset in your research, you should to refer to our work as the following BibTeX entry.

```
@inproceedings{Wang2019vehicle,
  title={Vehicle Re-identification in Aerial Imagery : Dataset and Approach},
  author={Peng, Wang and Bingliang, Jiao and Lu, Yang and Shizhou, Zhang and Wei, Wei and Yanning, Zhang},
  booktitle={Proc. IEEE Int. Conf. Comp. Vis.},
  year={2019}
} 
```


