from flask import Flask, jsonify, request
import psutil
import os
import socket

app = Flask(__name__)

@app.route("/status", methods=["GET"])
def status():
	mem = psutil.virtual_memory()
	mem = mem.total/(1024*1024*1024)
	memt = str(round(mem, 2)) +' GB'
	return jsonify ({'Hostname':socket.gethostname(), 'IP':request.remote_addr, 'No. of CPU\'s':psutil.cpu_count(), 'Memory':memt}), 400

if __name__ == '__main__':
	app.run(port=8080)
