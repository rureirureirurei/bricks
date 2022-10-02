# bricks
Python OpenCV solution to bricks counting problem.
## What is the bricks counting problem?
We have to tell the number of bricks pieces on a photo with the best precision possible. That's it.
## How does it work?

The algorithm consists of the following steps:
- Grayscaling
- Blurring
- Thresholding
- Removing minor artifacts
- Eroding
- Finding contours in the eroded image

#### Grayscaling
  We do grayscale image in order to make it one dimension instead of three and make the calculations easier and faster. The default OpenCV `CV.COLOR_BGR2GRAY` is used.
  
#### Blurring
  The gaussian blur with kernel size 9x9 improves accuracy of the contours finding related algorithms.
  
#### Thresholding
  After the grayscaling and blurring we apply adaptive thresholding with gaussian sum over the kernel with size 21x21 and constant of 3.
  
![thresh_Bricks_1](https://user-images.githubusercontent.com/78561567/193474881-abca9091-0072-45ac-a959-587c3f161b55.jpg)
![thresh_Bricks_2](https://user-images.githubusercontent.com/78561567/193474882-c7d35d4e-5584-4f63-bf78-33e90e8cf1a3.jpg)
![thresh_Bricks_3](https://user-images.githubusercontent.com/78561567/193474876-6f2a340b-d5cf-4851-886b-80cef0afdc5f.jpg)
![thresh_Bricks_4](https://user-images.githubusercontent.com/78561567/193474884-0044a157-e3f4-4216-a707-fd59197ba9cf.jpg)

That step makes finding separate objects incredibly easier.

#### Removing minor artifacts
  In order to reduce the number of mistakingly identified bricks after the eroding, we will remove the minor artifacts. At first, we are finding contours at the thresholed image and then fill the smallest with white. After this step is applied, number of artifacts is significatnly reduced.
  
  ![thresh_Bricks_1](https://user-images.githubusercontent.com/78561567/193475116-a58ede47-0879-4fbb-b5f3-75d13394561b.jpg)
![thresh_Bricks_2](https://user-images.githubusercontent.com/78561567/193475118-a12ceaf3-29dd-4e90-a9fb-1deae37de313.jpg)
![thresh_Bricks_3](https://user-images.githubusercontent.com/78561567/193475119-0dd1cb33-a29d-454c-bb19-b800380efba7.jpg)
![thresh_Bricks_4](https://user-images.githubusercontent.com/78561567/193475121-752334bb-4a03-4fe4-a9b3-5f2ac161c9fc.jpg)


#### Eroding
  The main problem left after the thresholding is applied are the bricks with identical colour 'glued' together. To fix this, we will apply eroding with the kernel of size 19x19 and initial values at -5. After the image is eroded, the amount of 'glued' bricks significantly reduces.
  
![thresh_Bricks_1](https://user-images.githubusercontent.com/78561567/193475236-a8673b99-d319-47f0-909c-a64bd646e7de.jpg)
![thresh_Bricks_2](https://user-images.githubusercontent.com/78561567/193475238-1797f709-ba1c-4014-b98a-bc94e2ba451a.jpg)
![thresh_Bricks_3](https://user-images.githubusercontent.com/78561567/193475240-7263641b-780d-4ac9-9ff1-1d8b8ec690d5.jpg)
![thresh_Bricks_4](https://user-images.githubusercontent.com/78561567/193475241-c14c1544-6e6d-4e96-bdf2-5d69727bc6da.jpg)

#### Counting contours
  The last step is basically counting contours on the eroded image.

![thresh_Bricks_1](https://user-images.githubusercontent.com/78561567/193475331-1a3efa5a-47e0-450f-a6ae-1e0034c38e3f.jpg)
![thresh_Bricks_2](https://user-images.githubusercontent.com/78561567/193475334-2123a4ed-b5ac-4d1d-aead-f284b0e7d945.jpg)
![thresh_Bricks_3](https://user-images.githubusercontent.com/78561567/193475336-c6cf4519-5080-4447-a3c6-d2ce846ca760.jpg)


![thresh_Bricks_4](https://user-images.githubusercontent.com/78561567/193475338-7aa3e881-c00c-4da2-8332-909581b17f00.jpg)

Given approach gives satisfying accuracy ~0.94 and processes given 4 images in 584 millis.

## Usage

### Installation
  To install the script simply paste this into console and press enter `git clone TODO`
  All the images should be placed into the `images` folder. TODO 

TODO
## Screenshots
