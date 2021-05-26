from flask import Flask, render_template, request, redirect
from discord.utils import snowflake_time
import datetime
import time
import pytz

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
	if request.method == "POST":
		try:
			snowflake_id = request.form["id"]
			tz = pytz.timezone("America/Los_Angeles")
			tz2 = tz.localize(datetime.datetime.now())
			snow_pst = snowflake_time(int(snowflake_id)).astimezone(tz)
			created_at = f'{datetime.datetime.strftime(snow_pst, "%A, %B %-d, %Y, %-I:%M:%S %p")} {tz2.tzname()}'
			timestamp = round(time.mktime(snowflake_time(int(snowflake_id)).timetuple()))
			iso = snowflake_time(int(snowflake_id))
			return redirect(f"https://www.snowflake-time.tk/?id={request.form['id']}") 
		except:
			return redirect("https://www.snowflake-time.tk/")
	
	if request.args.get("id"):
		try:
			snowflake_id = request.args.get("id")
			tz = pytz.timezone("America/Los_Angeles")
			tz2 = tz.localize(datetime.datetime.now())
			snow_pst = snowflake_time(int(snowflake_id)).astimezone(tz)
			created_at = f'{datetime.datetime.strftime(snow_pst, "%A, %B %-d, %Y, %-I:%M:%S %p")} {tz2.tzname()}'
			timestamp = round(time.mktime(snowflake_time(int(snowflake_id)).timetuple()))
			iso = snowflake_time(int(snowflake_id))
			return render_template("index.html", created_at=created_at, timestamp=timestamp, iso=iso, share_url=f"https://www.snowflake-time.tk/?id={snowflake_id}")
		except:
			return redirect("https://www.snowflake-time.tk/")
	
	return render_template("index.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080, debug=True)
