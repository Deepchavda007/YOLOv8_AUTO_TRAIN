import ultralytics
path = "autotrain_app/static/output/Yolov8_output/"

class YOLO_AUTO_TEST:
    def __init__(self):
        pass
    
    def Testing(self,dataset_path,model_name,device='cpu'):
        model =ultralytics.YOLO(model_name)
        #model.predictor.save_dir='test'
        model.predict(dataset_path,save=True,save_txt=True,project=path)
        
        return model.predictor.save_dir
        


        
if __name__== "__main__":

    ultralytics.checks()
    yolo_at_obj=YOLO_AUTO_TEST()
    predict_path=yolo_at_obj.Testing("/root/yolo_auto_train/testing/football_data/test/","deep/test_yolo/111_26/weights/best.pt",device=0)
    print(predict_path)
