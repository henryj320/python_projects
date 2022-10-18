

$(document).ready(function() {  // Entered when the page has finished loading.

    const weekMonday = $("#weekMonday")
    weekMonday.change(function() {  // When the week to add the gym sessions to is inputted.
        setDateToMonday(weekMonday)
    })

    const gymSessions = $("#gymSessions")
    const runSessions = $("#runSessions")
    const otherSessions = $("#otherSessions")
    const totalSessions = $("#totalSessions")

    // On change of number of gym sessions, runs or other sessions: Update total sessions.
    gymSessions.change(function() {
        setTotalSessions(totalSessions, gymSessions, runSessions, otherSessions)
    })
    runSessions.change(function() {
        setTotalSessions(totalSessions, gymSessions, runSessions, otherSessions)
    })
    otherSessions.change(function() {
        setTotalSessions(totalSessions, gymSessions, runSessions, otherSessions)
    })
})

// Changes the date set to the previous Monday. If it fails, then sends an alert.
function setDateToMonday(weekMonday) {
    
    let weekDayValue = weekMonday.val();  // Gets the value from the date input.

    let convertedToDate = new Date(weekDayValue)  // Converts it into a Date.

    let year = convertedToDate.getFullYear()
    let month = convertedToDate.getMonth() + 1
    let day = convertedToDate.getDate()


    if (day >= (7 - convertedToDate.getDay())) {
        dayOfWeek = convertedToDate.getDay() - 1  // Sunday = -1, Saturday = 5.
        dayOfWeek = dayOfWeek % 7

        if (dayOfWeek >= 1) {  // If not Sunday or Monday.
            day = day - dayOfWeek
        } else if (dayOfWeek == -1) {  // If a Sunday was selected.
            day = day - 6;
        }
    }

    if (month < 10) {  // Adds a "0" if required.
        month = String("0" + month)
    }

    if (day < 10) {  // Adds a "0" if required.
        day = String("0" + day)
    }

    let closestMonday = year + "-" + month + "-" + day;
    weekMonday.val(closestMonday);

    mondayCheck = new Date(closestMonday) 

    if (mondayCheck.getDay() != 1) {
        alert("Please select a Monday");
    }
}


function setTotalSessions(totalSessions, gym, run, other) {
    gymValue = parseInt(gym.val())
    runValue = parseInt(run.val())
    otherValue = parseInt(other.val())

    totalSessions.val(gymValue + runValue + otherValue)
}
