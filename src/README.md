<h1 align="center">TEDU LECTURES - SOURCE TO SCRAPE</h1>

### Scrapes all lectures' GPA and related information from TEDUPortal, database of TED University that is open to all of its students. 

<br>

## Turkish
Not: Veriyi çekebilmek için TED Üniversitesi öğrencisi olmanız gerekmektedir (Portal sistemine giriş yapabilmek için).

Portaldaki veriyi scrape etmek için aşağıdaki adımlar izlenmelidir:


1. Bu repo'yu bilgisayarınıza clonelayın.
    
    ```git clone https://github.com/senceryucel/Tedu-Lectures.git```

2. Gerekli kütüphaneleri indirin.
    
    ```pip install -r requirements.txt```

3. <b>src</b> klasörü içerisindeki <b>config.json</b> dosyasını dilediğiniz şekilde configure edin.

4. Database kullanacaksanız gerekli postgresql bağlantılarınızı yaptığınıza emin olun. Eğer database kullanmak istemiyorsanız, <b>use_database</b> değişkenini <b>false</b> yapmayı unutmayın.

5. <b>src</b> klasörü içerisindeki <b>main.py</b> scripti, verinin scrape işlemini başlatacaktır.

    ```python main.py```

<br><br>

## English
Note: You have to be a student of TEDU to scrape the data (to be able to log in to  TEDUPortal).

Below steps should be followed to scrape the data in TeduPortal:

1. Clone this repository to your PC.
    
    ```git clone https://github.com/senceryucel/Tedu-Lectures.git```

2. Install dependencies.
    
    ```pip install -r requirements.txt```

3. Configure the file named <b>config.json</b> in the folder <b>src</b> as however you want it to be.

4. Make sure you have successfully built your postgresql connections if you wish to copy the data into a database. If you are not going to use any database, do not forget to change the variable named <b>use_database</b> to <b>false</b>.

5. You can start the process with using the script <b>main.py</b> located under the folder <b>src</b>.

    ```python src/main.py```