from flask import Flask, render_template, request, redirect
import discord
from discord.utils import snowflake_time
import datetime
import requests
import time

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
	if request.method == "POST":
		try:
			snowflake_id = request.form["id"]
			created_at = f'{datetime.datetime.strftime(snowflake_time(int(snowflake_id)), "%A, %B %-d, %Y, %-I:%M:%S %p")} UTC'
			timestamp = round(time.mktime(snowflake_time(int(snowflake_id)).timetuple()))
			iso = snowflake_time(int(snowflake_id))
			return render_template("index.html", created_at=created_at, timestamp=timestamp, iso=iso)
		except:
			return redirect('https://snowflaketime.mythify.repl.co/')
	
	return render_template("index.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080, debug=True)
