from flask import Flask, render_template, g
import csv
import sqlalchemy as db

app=Flask(__name__) # __name__ 代表目前執行的模組

# sql setting
path_to_db = "./db/0050.db"
table = '0050'
engine = db.create_engine(f'sqlite:///{path_to_db}')
# connection  = engine.connect()
metadata = db.MetaData()
table_0050 = db.Table(table, metadata, autoload=True, autoload_with=engine)

@app.route("/") # 函式的裝飾(Decorator): 以函式為基礎，提供附加的功能
def home():
    return render_template('index.html')

@app.route("/index.html") # 
def index():
    return render_template('index.html')

@app.route("/charts.html")
def charts():
    return render_template('charts.html')

@app.route("/401.html")
def m401():
    return render_template('401.html')

@app.route("/404.html")
def m404():
    return render_template('404.html')

@app.route("/500.html")
def m500():
    return render_template('500.html')

# connection sql
@app.route("/data")
def data():
    connection  = engine.connect() # connection 要放在view function中，否則會出現thread error
    query = db.select(func.count()).select_from(table_0050)
    proxy = connection.execute(query)

    # Close connection
    connection.close()


     return render_template('data.html')








if __name__=="__main__": # 如果以主程式執行
    app.run(debug=True) # 立刻啟動伺服器