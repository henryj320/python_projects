

$(document).ready(function() {  // Entered when the page has finished loading.

    const weekMonday = $("#weekMonday");
    weekMonday.change(function() {  // When the week to add the gym sessions to is inputted.
        setDateToMonday(weekMonday);
    })

    const gymSessions = $("#gymSessions");
    const runSessions = $("#runSessions");
    const otherSessions = $("#otherSessions");
    const totalSessions = $("#totalSessions");

    // On change of number of gym sessions, runs or other sessions: Update total sessions.
    gymSessions.change(function() {
        setTotalSessions(totalSessions, gymSessions, runSessions, otherSessions);
    })
    runSessions.change(function() {
        setTotalSessions(totalSessions, gymSessions, runSessions, otherSessions);
    })
    otherSessions.change(function() {
        setTotalSessions(totalSessions, gymSessions, runSessions, otherSessions);
    })

    let highestSpecObligation = 1;
    let latestSpecExercise = $("#exercise" + highestSpecObligation);
    let latestSpecDay = $("#day" + highestSpecObligation);
    let enabled = true;

    latestSpecDay.change(function() {
        if (enabled) {

            addSpecificObligation(latestSpecDay, highestSpecObligation, otherSessions)

            highestSpecObligation = highestSpecObligation + 1
    
            enabled = false
        }

        // // Nested onChange() so that you can add an unlimited number 
        // latestSpecDay = $("#day" + highestSpecObligation);
        // latestSpecDay.change(function() {
        //     addSpecificObligation(latestSpecDay, highestSpecObligation)
        // })

    })

})

// Changes the date set to the previous Monday. If it fails, then sends an alert.
function setDateToMonday(weekMonday) {
    
    let weekDayValue = weekMonday.val();  // Gets the value from the date input.

    let convertedToDate = new Date(weekDayValue);  // Converts it into a Date.

    let year = convertedToDate.getFullYear();
    let month = convertedToDate.getMonth() + 1;
    let day = convertedToDate.getDate();


    if (day >= (7 - convertedToDate.getDay())) {
        dayOfWeek = convertedToDate.getDay() - 1;  // Sunday = -1, Saturday = 5.
        dayOfWeek = dayOfWeek % 7;

        if (dayOfWeek >= 1) {  // If not Sunday or Monday.
            day = day - dayOfWeek;
        } else if (dayOfWeek == -1) {  // If a Sunday was selected.
            day = day - 6;
        }
    }

    if (month < 10) {  // Adds a "0" if required.
        month = String("0" + month);
    }

    if (day < 10) {  // Adds a "0" if required.
        day = String("0" + day);
    }

    let closestMonday = year + "-" + month + "-" + day;
    weekMonday.val(closestMonday);

    mondayCheck = new Date(closestMonday) 

    if (mondayCheck.getDay() != 1) {
        alert("Please select a Monday");
    }
}


function setTotalSessions(totalSessions, gym, run, other) {
    gymValue = parseInt(gym.val());
    runValue = parseInt(run.val());
    otherValue = parseInt(other.val());

    totalSessions.val(gymValue + runValue + otherValue);
}


function addSpecificObligation(latestSpecDay, previousNumber, otherSessions) {

    otherSessionsVal = otherSessions.val()
    otherSessions.val(parseInt(otherSessionsVal) + 1)

    let nextNumber = previousNumber + 1
    
    //console.log(latestSpecDay.attr("id"))

    // Creates a new opening span.    
    let openSpan = $("<span>", {
        text: "I have"
    });
    $("#specificDays").append(openSpan)

    
    // Creates a new <select> for the exercise.
    let newExerciseSelect = $("<select>", {
        id: "exercise" + nextNumber,
        name: "exercise" + nextNumber
    });


    // Adds each of the options to the <select> above
    let selectExerciseOption = $("<option>", {
        value: "not_selected_exercise",
        text: "Select Exercise"
    });
    newExerciseSelect.append(selectExerciseOption);

    let canoePoloOption = $("<option>", {
        value: "canoe_polo",
        text: "Canoe Polo"
    });
    newExerciseSelect.append(canoePoloOption);

    let kayakingOption = $("<option>", {
        value: "kayaking",
        text: "Kayaking"
    });
    newExerciseSelect.append(kayakingOption);

    let boulderingOption = $("<option>", {
        value: "bouldering",
        text: "Bouldering"
    });
    newExerciseSelect.append(boulderingOption);

    let otherOption = $("<option>", {
        value: "other",
        text: "Other"
    });
    newExerciseSelect.append(otherOption);


    // Adds the new <select> to the div
    $("#specificDays").append(newExerciseSelect);


    let midSpan = $("<span>", {
        text: "on a"
    });
    $("#specificDays").append(midSpan)

    // Creates a new <select> for the day.
    let newDaySelect = $("<select>", {
        id: "day" + nextNumber,
        name: "day" + nextNumber
    });

    // Adds each of the options to the <select> above
    let selectDayOption = $("<option>", {
        value: "not_selected_day",
        text: "Select Day"
    });
    newDaySelect.append(selectDayOption);

    let monOption = $("<option>", {
        value: "monSpec",
        text: "Monday"
    });
    newDaySelect.append(monOption);

    let tuesOption = $("<option>", {
        value: "tuesSpec",
        text: "Tuesday"
    });
    newDaySelect.append(tuesOption);

    let wedOption = $("<option>", {
        value: "wedSpec",
        text: "Wednesday"
    });
    newDaySelect.append(wedOption);

    let thursOption = $("<option>", {
        value: "thursSpec",
        text: "Thursday"
    });
    newDaySelect.append(thursOption);

    let friOption = $("<option>", {
        value: "friSpec",
        text: "Friday"
    });
    newDaySelect.append(friOption);

    let satOption = $("<option>", {
        value: "satSpec",
        text: "Saturday"
    });
    newDaySelect.append(satOption);

    let sunOption = $("<option>", {
        value: "sunSpec",
        text: "Sunday"
    });
    newDaySelect.append(sunOption);


    $("#specificDays").append(newDaySelect);

    newDaySelect.on("change", function(event) {
        addSpecificObligation(this, nextNumber)
    })


    // TODO: FIX SO THAT PREVIOUS SELECTS CANT ALSO MAKE A NEW ONE
    // latestSpecDay.off("change")

    $("#specificDays").append($("<br>"));
    $("#specificDays").append($("<br>"));


    // $("#monCheck").toggle(this.checked);
    
    // $("#monCheck").attr("checked")
    $("#monCheck").prop("checked", true)
}
