import json
from datetime import datetime, timedelta

with open("shift.json") as f:
  data = json.load(f)
start = datetime.fromisoformat(data["shift"]["start"])
end = datetime.fromisoformat(data["shift"]["end"])

def isWeekend(d):
  if d.isoweekday() > 5:
    return True
  return False

def getShift(dt): #date and time
  d = dt.strftime("%Y-%m-%d") #date
  t = dt.strftime("%H:%M:%S") #time
  T = datetime.strptime(t,"%H:%M:%S")
  if isWeekend(dt):
    print(dt,"is weekend")
    eDs = data["roboRate"]["extraDay"]["start"] #extraDayStart
    eDe = data["roboRate"]["extraDay"]["end"] #extraDayEnd
    eNs = data["roboRate"]["extraNight"]["start"] #extraNightStart
    eNe = data["roboRate"]["extraNight"]["end"] #extraNightEnd
    eDsT = datetime.strptime(eDs,"%H:%M:%S")
    eDeT = datetime.strptime(eDe,"%H:%M:%S")
    eNsT = datetime.strptime(eNs,"%H:%M:%S")
    eNeT = datetime.strptime(eNe,"%H:%M:%S")
    if eDsT <= eDeT: #same day, most possible
      if eDsT <= T < eDeT:
        print("time in day, extra, same shift date")
        shiftStart = datetime.fromisoformat(d + 'T' + t)
        shiftEnd = datetime.fromisoformat(d + 'T' + eDe)
        shift = "extraDay"
    elif eDsT > eDeT:
      if eDsT <= T:
        print("time in day, extra, shift date + 1")
        shiftStart = datetime.fromisoformat(d + 'T' + t)
        shiftEnd = datetime.fromisoformate(d + 'T' + "00:00:00")
        #shiftEnd = datetime.fromisoformat(d + 'T' + eDe)
        shiftEnd = shiftEnd + timedelta(days = 1)
        shift = "extraDay"
      elif T < eDeT: #shiftEnd and T have same date
        print("time in day, extra, same shift date")
        shiftStart = datetime.fromisoformat(d + 'T' + t)
        shiftEnd = datetime.fromisoformat(d + 'T' + eDe)
        shift = "extraDay"
    if eNsT <= eNeT:
      if eNsT <= T < eNeT:
        print("time in night, extra, same shift date") #although in the question night shift always cross dates, so this should never happen conventionally
        shiftStart = datetime.fromisoformat(d + 'T' + t)
        shiftEnd = datetime.fromisoformat(d + 'T' + eNe)
        shift = "extraNight"
    elif eNsT > eNeT: #in the question, night shift always cross dates
      if eNsT <= T: 
        print("time in night, extra, shift date + 1")
        shiftStart = datetime.fromisoformat(d + 'T' + t)
        shiftEnd = datetime.fromisoformat(d + 'T' + "00:00:00")
        #shiftEnd = datetime.fromisoformat(d + 'T' + eNe)
        shiftEnd = shiftEnd + timedelta(days = 1)
        shift = "extraNight"
      elif T < eNeT:
        print("time in night, extra, same shift date")
        shiftStart = datetime.fromisoformat(d + 'T' + t)
        shiftEnd = datetime.fromisoformat(d + 'T' + eNe)
        shift = "extraNight"
  else:
    print(dt,"is weekday")
    sDs = data["roboRate"]["standardDay"]["start"] #standardDayStart
    sDe = data["roboRate"]["standardDay"]["end"] #standardDayEnd
    sNs = data["roboRate"]["standardNight"]["start"] #standardNightStart
    sNe = data["roboRate"]["standardNight"]["end"] #standardNightEnd
    sDsT = datetime.strptime(sDs,"%H:%M:%S")
    sDeT = datetime.strptime(sDe,"%H:%M:%S")
    sNsT = datetime.strptime(sNs,"%H:%M:%S")
    sNeT = datetime.strptime(sNe,"%H:%M:%S")
    if sDsT <= sDeT: #same day, most possible
      if sDsT <= T < sDeT:
        print("time in day, weekday, same shift date")
        shiftStart = datetime.fromisoformat(d + 'T' + t)
        shiftEnd = datetime.fromisoformat(d + 'T' + sDe)
        shift = "standardDay"
    elif sDsT > sDeT:
      if sDsT <= T:
        print("time in day, weekday, shift date + 1")
        shiftStart = datetime.fromisoformat(d + 'T' + t)
        shiftEnd = datetime.fromisoformate(d + 'T' + "00:00:00")
        #shiftEnd = datetime.fromisoformat(d + 'T' + sDe)
        shiftEnd = shiftEnd + timedelta(days = 1)
        shift = "standardDay"
      elif T < sDeT: #shiftEnd and T have same date
        print("time in day, weekday, same shift date")
        shiftStart = datetime.fromisoformat(d + 'T' + t)
        shiftEnd = datetime.fromisoformat(d + 'T' + sDe)
        shift = "standardDay"
    if sNsT <= sNeT:
      if sNsT <= T < sNeT:
        print("time in night, weekday, same shift date") #although in the question night shift always cross dates, so this should never happen conventionally
        shiftStart = datetime.fromisoformat(d + 'T' + t)
        shiftEnd = datetime.fromisoformat(d + 'T' + sNe)
        shift = "standardNight"
    elif sNsT > sNeT: #in the question, night shift always cross dates
      if sNsT <= T: 
        print("time in night, weekday, shift date + 1")
        shiftStart = datetime.fromisoformat(d + 'T' + t)
        shiftEnd = datetime.fromisoformat(d + 'T' + "00:00:00")
        #shiftEnd = datetime.fromisoformat(d + 'T' + sNe)
        shiftEnd = shiftEnd + timedelta(days = 1)
        shift = "standardNight"
      elif T < sNeT:
        print("time in night, weekday, same shift date")
        shiftStart = datetime.fromisoformat(d + 'T' + t)
        shiftEnd = datetime.fromisoformat(d + 'T' + sNe)
        shift = "standardNight"
  rate = data["roboRate"][shift]["value"] * 60
  return shiftStart, shiftEnd, rate

restIdx = 0
salary = 0
shiftStart, shiftEnd, rate = getShift(start)
while shiftEnd < end:
  duration = (shiftEnd - start).total_seconds() / 3600
  print("duration",duration)
  prev_restIdx = restIdx
  restIdx += duration
  print("restIdx", restIdx)
  if restIdx > 8:
    print("takes some rest")
    duration = 8 - prev_restIdx
    print("break time start")
    start = start + timedelta(hours = duration + 1)
    salary += duration * rate
    print("start",start)
    print("salary",salary)
    restIdx = 0
    print("restIdx",restIdx)
    shiftStart, shiftEnd, rate = getShift(start)
  else:
    salary += duration * rate
    print("salary",salary)
    start = start + timedelta(hours = duration)
    print("start",start)
    shiftStart, shiftEnd, rate = getShift(start)
print("exited loop")
shiftStart, shiftEnd, rate = getShift(start)
duration = (end - start).total_seconds() / 3600
print(" duration", duration)
prev_restIdx = restIdx
restIdx += duration
print("restIdx",restIdx)
while restIdx > 8:
  duration = 8 - prev_restIdx
  print("duration before break",duration)
  start = start + timedelta(hours = duration + 1)
  salary += duration * rate
  if start > end:
    duration = 0
    break
  duration = (end - start).total_seconds() / 3600
  restIdx = duration
  prev_restIdx = 0
  print("salary",salary)
  print("restIdx",restIdx)

salary += duration * rate
print("Final salary",int(salary))

output = { "value": int(salary) }
with open("output.json", "w") as json_file:
  json.dump(output, json_file)