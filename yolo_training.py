import ultralytics
import yaml
import os


class YOLO_AUTO_TRAIN:
    def __init__(self):
        pass
    
    def Create_yaml(self,class_names,num_class,train_dataset_path,val_dataset_path,user_name,project_name):

        yaml_string=dict(train=train_dataset_path,val=val_dataset_path,nc=num_class,names=class_names)
        with open(user_name+"/"+project_name+"/data.yaml","w") as yaml_file:
            yaml.dump(yaml_string,yaml_file, default_flow_style=False,sort_keys=False)
            
    def Create_folder(self,user_name,project_name):
        if not os.path.exists(user_name):
            os.makedirs(user_name)
        if not os.path.exists(user_name+"/"+project_name):
            os.makedirs(user_name+"/"+project_name)
        
    
    
    def training(self,user_name ,val_dataset_path ,train_dataset_path ,class_names ,num_class ,model_name="yolov8m.pt" ,pretrained=False ,project_name="YOLO_V8" ,experiment_name="test1_" ,save_model_name='model.pt' ,num_epochs=20 ,imgsz=640 ,batch_size=-1 ,device="cpu"):
            print("=============== Start Training ================")
            user_name=user_name
            self.Create_folder(user_name,project_name)
            data=self.Create_yaml(class_names,num_class,train_dataset_path,val_dataset_path,user_name,project_name)
            #data="data.yaml"
            model = ultralytics.YOLO(model_name)

            model.train(data=user_name+"/"+project_name+"/data.yaml",
                                epochs=num_epochs,
                                batch=batch_size,
                                device=device,
                                project=user_name+"/"+project_name,
                                name=experiment_name,
                                pretrained=pretrained, 
                                imgsz=imgsz,
                               )

            #Export Model returns path where model is saved
            model_save_path =model.export()
            model_save_path=model_save_path.split(".")
            model_save_path[-1]=".pt"
            model_save_path="".join(model_save_path)
            new_model_save_path=model_save_path.replace("best.pt",str(save_model_name)+".pt")
            #------------------#
            os.rename(model_save_path,new_model_save_path)
            return new_model_save_path
        
    
    
if __name__== "__main__":
    
    ultralytics.checks()
    yolo_at_obj=YOLO_AUTO_TRAIN()
    
    # model_name={'detection': ['yolov8n.pt','yolov8s.pt','yolov8m.pt','yolov8l.pt','yolov8x.pt']}

    model_save_path= yolo_at_obj.training("deep" ,"C:/Users/DEEP/OneDrive/Desktop/Yolo_auto_train/dataset/val/images","C:/Users/DEEP/OneDrive/Desktop/Yolo_auto_train/dataset/train/images" ,["Players","Football"], 2 ,"yolov8s.pt" ,False ,"test_yolo" ,"111_","deep",1,640,16)
        
        