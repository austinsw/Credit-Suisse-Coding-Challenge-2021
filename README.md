# Credit-Suisse-Coding-Challenge-2021

## Question

It is the year 2038 and robots have the right to get paid for the work they do. As an employer of robots, you need to calculate how much a robot gets paid for cleaning your apartment.

How much a robot gets paid depends on when you ask the robot to work. After all, during the day the robot can be a little louder and work a bit faster whilst everyone is out of the house, but at night, you will need to turn on the super quiet mode, which takes more effort! Robots also cost a bit more over weekends, due to higher demand.

Your robot rates calculator needs to consider the following:

- A standard minutely rate for weekdays, and an ‘extra’ rate for weekends.
- When rates switches between day and night rates, for a total of four different rates (weekday/weekend + day/night).
- For every eight hours, the robot needs to take an hour of unpaid break (or part thereof) for planned system maintenance.

Implement an application that can take in an input like the example below, and provide an output as shown:
```json
{
"shift": {
"start": "2038-01-01T20:15:00",
"end": "2038-01-02T04:15:00"
},
"roboRate": {
"standardDay": {
"start": "07:00:00",
"end": "23:00:00",
"value": 20
},
"standardNight": {
"start": "23:00:00",
"end": "07:00:00",
"value": 25
},
"extraDay": {
"start": "07:00:00",
"end": "23:00:00",
"value": 30
},
"extraNight": {
"start": "23:00:00",
"end": "07:00:00",
"value": 35
}
}
}
```
Sample output:

`{ "value": 13725 }`

Additional test cases for the sample rates above:

| Start | End | Expected value |
| ----- | --- | -------------- |
| 2038-01-01T20:15:00 | 2038-01-02T08:15:00 | 19650 |
| 2038-01-11T07:00:00 | 2038-01-17T19:00:00 | 202200 |
| 2038-01-01T20:15:00 | 2038-01-02T04:16:00 | 13725 |
| 2038-01-01T20:15:00 | 2038-01-02T05:16:00 | 13760 |

The problem statement has not been completely described - you should provide comments on any other assumptions you have made on top of these two:

1. Shift timestamps will be given in ISO format “yyyy-MM-dd’T’hh:mm:ss”, rates in “hh:mm:ss”.
2. Duration boundaries are \[inclusive, exclusive), e.g. a shift from 7 am to 11 pm will fit into a single day rate, without incurring a minute of the night rate.

## My Notes & Assumptions

Since it is impossible to take an input in json fomat through the console, I assumed the input file would be within the same directory as the main.py with the name "shift.json". The output would also be in json format in a file called "output.json".

The trickiest part of this question is to consider the cases where the working hour crosses day, night, weekday and weekend. So we need to break down the "shift time" for every case of crossing between day and night (in the question example, it's usually 07:00, 23:00) and everytime it crosses day (00:00) as it may cross from a weekday into weekend and vice versa.

After that, a restIdx is also implemented to give the robot 1 hour of breaktime for every accumulated 8 hours of work. Then it's just summation of multiplication between work time and rate.

Note: Although the question sample did not specify, I also consider the general cases where the start time and end time for the shifts in weekend and weekday can be different. I also consider cases where day and night may or may not cross dates (for example, night could be from 00:00 - 07:00 and day could be 07:00 - 00:00) to make the programme more flexible.

**Note that the code is developed on Replit, so the libraries used are Replit specific!**
