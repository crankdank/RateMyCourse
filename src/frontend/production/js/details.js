async function populate() {
  const params = new URLSearchParams((new URL(window.location.href)).search);

  const subject = params.get("subj");
  const courseNumber = params.get("num");

  let courseInfo = {
    "faculty": "Science",
    "subject": "CMPUT",
    "course_num": "401",
    "average_overall": 4.5,
    "average_workload": 3.1,
    "average_interest": 4.5,
    "average_usefulness": 5.0,
    "average_difficulty": 2.0,
    "assignedProfs": "TBA",
    "hasLab": false
  }

  courseInfo = (await (await fetch(`http://localhost:8000/subject/${subject}/number/${courseNumber}`)).json())[0];

  const data = {
    datasets: [{
      data: [courseInfo.average_overall, 5 - courseInfo.average_overall],
      backgroundColor: [
        'rgb(39, 93, 56)',
        'rgba(255, 255, 255, 0)'
      ],
      hoverOffset: 4
    }]
  };

  const config = {
    type: 'doughnut',
    data: data,
    options: {
      plugins: {
        tooltip: {
          enabled: false
        }
      },
      events: [],
      cutout: "65%"
    }
  };

  const myChart = new Chart(
    document.getElementById('doughnutChart'),
    config
  );

  document.querySelector("p.back").addEventListener("click", (e) => {
    window.open("./index.html", "_self");
  })

  // Set all course data
  document.querySelector("#title").innerHTML = `${courseInfo.subject} ${courseInfo.course_num}`;
  window.document.title = `${courseInfo.subject} ${courseInfo.course_num}`;
  document.querySelector("#fac").innerHTML = `Faculty of ${courseInfo.faculty}`;
  document.querySelector("#overallRating").innerHTML = `${courseInfo.average_overall.toFixed(1)}`;
  document.querySelector("#diff").innerHTML = `${courseInfo.average_difficulty.toFixed(1)}`;
  document.querySelector("#use").innerHTML = `${courseInfo.average_usefulness.toFixed(1)}`;
  document.querySelector("#work").innerHTML = `${courseInfo.average_workload.toFixed(1)}`;
  document.querySelector("#interest").innerHTML = `${courseInfo.average_interest.toFixed(1)}`;
}

populate();
