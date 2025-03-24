let month = "March"; // Change this to test different months

let sign = "";
if (month === "January") {
    sign = "Capricorn ♑";
} else if (month === "February") {
    sign = "Aquarius ♒";
} else if (month === "March") {
    sign = "Pisces ♓";
} else if (month === "April") {
    sign = "Aries ♈";
} else if (month === "May") {
    sign = "Taurus ♉";
} else if (month === "June") {
    sign = "Gemini ♊";
} else if (month === "July") {
    sign = "Cancer ♋";
} else if (month === "August") {
    sign = "Leo ♌";
} else if (month === "September") {
    sign = "Virgo ♍";
} else if (month === "October") {
    sign = "Libra ♎";
} else if (month === "November") {
    sign = "Scorpio ♏";
} else if (month === "December") {
    sign = "Sagittarius ♐";
} else {
    console.log("Error: Invalid month entered.");
}

// If a valid month was entered, generate a random fortune
if (sign !== "") {
    let randomNumber = Math.floor(Math.random() * 5); // Generates a number between 0-4

    let fortune = "";
    if (randomNumber === 0) {
        fortune = "This is the month to set big goals—your hard work will pay off soon!";
    } else if (randomNumber === 1) {
        fortune = "A surprise message will change your day.";
    } else if (randomNumber === 2) {
        fortune = "Your confidence will open new doors.";
    } else if (randomNumber === 3) {
        fortune = "A lucky break is just around the corner!";
    } else if (randomNumber === 4) {
        fortune = "Your energy will attract exciting new opportunities.";
    }

    console.log(`Your Zodiac sign is ${sign}.`);
    console.log(`Your horoscope today: ${fortune}`);
}
