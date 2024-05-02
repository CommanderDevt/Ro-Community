from flask import Flask, render_template,jsonify
import psutil
from werkzeug.sansio.response import Response

app = Flask(__name__)

@app.route('/')
def index():
  f = open("index.json", "r")
  return f.read()
  f.close()


@app.route('/update/<function>/<plr>')
def update(function, plr):
  global status
  playertarget = plr
  f = open("index.json", "r")
  Response = f.read()
  if function == "join":
    status = "Join"
    #currentplayers = open("player.txt", "r")
    #startop = int(currentplayers.read())
    #writeplayers = open("player.txt", "w")
    #floattowrite = str(startop + 1)
    #writeplayers.write(floattowrite)
    #print(currentplayers.read())
    #currentplayers.close()
    #writeplayers.close()
    Response = {
      "Return": [239]
    }
  if function == "leave":
    status = "Leave"
    currentplayers = open("player.txt", "r")
    startop = int(currentplayers.read())
    writeplayers = open("player.txt", "w")
    floattowrite = str(startop - 1)
    writeplayers.write(floattowrite)
    print(currentplayers.read())
    currentplayers.close()
    writeplayers.close()
  playersinserver = open("player.txt", "r")
  print(plr)
  playersinserver.close
  return Response
  f.close()


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
