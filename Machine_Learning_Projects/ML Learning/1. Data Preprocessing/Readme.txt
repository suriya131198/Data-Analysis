Data Preprocessing

    In this we will be learning 
        1. Data Cleaning/Processing
            we will be calculating mean value and will fill the empty cells with the mean value in it.
        2. Encoding Categorical Data
            i) OneHotEncoding
            ii) LabelEncoding
        3. Splitting DataSet
            we need to split the dataset into Train data & Test data
            i) Train data will consume most of the data and will train the model to predict the value/result
            ii) Test data will test the trained model and check whether the model is giving proper prediction or not.
        4. Feature Scaling
            This method will assign oru data by spitting them between specific value.
            It has 2 methods in it,
            i) Standardization:
                
                x(stand) = (x-mean(x))/StandardDeviation(x)
                
                This method will fit the data from -3 to 3.
            
            ii) Normalization:
            
                x(Norm) = (x-min(x))/(max(x)-min(x))
                
                This method will fit the data from 0 to 1.