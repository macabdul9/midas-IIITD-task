# midas-IIITD-task



#### Each subdirectory contains a requirements.txt file which has all the dependencies required to run the notebook it can be install using the command:
- pip install -r requirements.txt --user



### All the notebooks were coded on google colaboratory https://colab.research.google.com/. One can run the notebook by following the below mentioned instructions:
- Active internet connection is needed.
- Upload the dataset (not in case of amazon-planet problem) in .zip or any other  compressed format on googledrive
- Open google colab with same account as the googledrive where you have uploaded the dataset
- Clone this repository and upload the notebook along with its requirments.txt file on colaboratory. Notebook can be uploaded                         
  using file menu section while external files can be upoaded using below sript:
  
    from googel.colab import files
    uploaded = files.upload()
    
- Mount the coloboratory storage with the google drive using the following scripts:

    from google.colab import drive
    drive.mount('/content/drive')
    
 you will be redirected to a page asking for a authorization code associated with you google acccount(on which you have uploaded               the dataset)
 - start running the notebook cell sequentially after install the dependencies using above mentioned command

Note: check the path of the files and folder properly


  
  
  

