import pandas as pd
import numpy as np
import os
import shutil
from sklearn import model_selection
from tqdm import tqdm
import ast
DATA_PATH = 'C:/Users/kareem/Downloads/Compressed/archive/Surgical-Dataset/'
OUTPUT_PATH = 'C:/Users/kareem/Downloads/Compressed/yolov5-master/yolov5-master/tools-data/'


def process_data(data, data_type="train"):
     for _, row in tqdm(data.iterrows(), total=len(data)):
         yolo_data = []
         image_name = row["image_id"]
         image_name.replace('.txt', '')
         width = float(row["width"])
         height = row["height"] 
         x = row["x"] 
         y = row["y"]   
         x_center = x + width / 2
         y_center = y + height / 2
         x_center /= 640.0
         y_center /= 480.0
         width /= 640.0
         height /= 480.0
         yolo_data.append([image_name, x_center, y_center, width, height])
         yolo_data = np.array(yolo_data)
         np.savetxt(
             os.path.join(OUTPUT_PATH, f"Labels/{data_type}/{image_name}.txt",
             yolo_data,
             fmt = ["%d", "%f", "%f", "%f", "%f"])
          )
         shutil.copyfile(
              os.path.join(DATA_PATH, f"Images/All/images/{image_name}.jpg"),
            os.path.join(OUTPUT_PATH, f"images/{data_type}/{image_name}.jpg")  
          )


if __name__ == "__main__":
     df = pd.read_csv("Copyoftrain.csv")
     df_width = df.loc[:,["width"]].apply(ast.literal_eval)
     df_height = df.loc[:,["height"]].apply(ast.literal_eval)
     df_x = df.loc[:,["x"]].apply(ast.literal_eval)
     df_y = df.loc[:,["y"]].apply(ast.literal_eval)
     df = df.groupby ("image_id")["width","height","x","y"].apply(list).reset_index(name="bboxes")
                 
     df_train, df_valid  = model_selection.train_test_split(df, 
     test_size=0.1,
     random_state=42, 
     shuffle=True)
     df_train = df_train.reset_index(drop = True)
     df_valid = df_valid.reset_index(drop = True)

process_data(df_train, data_type="train")
process_data(df_valid, data_type="validation")
