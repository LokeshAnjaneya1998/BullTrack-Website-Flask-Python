async function cmonth(table) {
  const response = await fetch('/chartdata');
  const data = await response.json();

  const wishchart = data.wishchart.map(item => item.applied_on);
  const inpchart = data.inpchart.map(item => item.applied_on);
  const appchart = data.appchart.map(item => item.applied_on);
  const offchart = data.offchart.map(item => item.applied_on);

  var chartfetch = "";
  if (table == 'wish') {
    chartfetch = wishchart;
  }
  if (table == 'inp') {
    chartfetch = inpchart;
  }
  if (table == 'app') {
    chartfetch = appchart;
  }
  if (table == 'off') {
    chartfetch = offchart;
  }

  var janCount = 0; var febCount = 0; var marchCount = 0; var aprilCount = 0; var mayCount = 0; var juneCount = 0;
  var julyCount = 0; var augCount = 0; var sepCount = 0; var octCount = 0; var novCount = 0; var decCount = 0;
  for (const job of chartfetch) {
    console.log(table + job);
    var appMonth = job.split("-")[1];
    if (appMonth == 01) { janCount++; }
    if (appMonth == 02) { febCount++; }
    if (appMonth == 03) { marchCount++; }
    if (appMonth == 04) { aprilCount++; }
    if (appMonth == 05) { mayCount++; }
    if (appMonth == 06) { juneCount++; }
    if (appMonth == 07) { julyCount++; }
    if (appMonth == 08) { augCount++; }
    if (appMonth == 09) { sepCount++; }
    if (appMonth == 10) { octCount++; }
    if (appMonth == 11) { novCount++; }
    if (appMonth == 12) { decCount++; }
  }
  localStorage.setItem(table + 'janCount', janCount);
  localStorage.setItem(table + 'febCount', febCount);
  localStorage.setItem(table + 'marchCount', marchCount);
  localStorage.setItem(table + 'aprilCount', aprilCount);
  localStorage.setItem(table + 'mayCount', mayCount);
  localStorage.setItem(table + 'juneCount', juneCount);
  localStorage.setItem(table + 'julyCount', julyCount);
  localStorage.setItem(table + 'augCount', augCount);
  localStorage.setItem(table + 'sepCount', sepCount);
  localStorage.setItem(table + 'octCount', octCount);
  localStorage.setItem(table + 'novCount', novCount);
  localStorage.setItem(table + 'decCount', decCount);

}

function monNum(table, mon) {
  var monthValue = localStorage.getItem(table + mon + 'Count');
  return monthValue;

}
const data = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
  datasets: [{
    label: 'wish List',
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgba(54, 162, 235, 1)',
    borderWidth: 1,
    data: [monNum('wish', 'jan'), monNum('wish', 'feb'), monNum('wish', 'march'), monNum('wish', 'april'), monNum('wish', 'may')
      , monNum('wish', 'june'), monNum('wish', 'july'), monNum('wish', 'aug'), monNum('wish', 'sep'), monNum('wish', 'oct')
      , monNum('wish', 'nov'), monNum('wish', 'dec')],
  },
  {
    label: 'Applied',
    backgroundColor: 'rgba(139, 0, 139, 0.2)',
    borderColor: 'rgba(139, 0, 139, 1)',
    borderWidth: 1,
    data: [monNum('app', 'jan'), monNum('app', 'feb'), monNum('app', 'march'), monNum('app', 'april'), monNum('app', 'may')
      , monNum('app', 'june'), monNum('app', 'july'), monNum('app', 'aug'), monNum('app', 'sep'), monNum('app', 'oct')
      , monNum('app', 'nov'), monNum('app', 'dec')],
  },
  {
    label: 'Applications In-Process',
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgba(255, 99, 132, 1)',
    borderWidth: 1,
    data: [monNum('inp', 'jan'), monNum('inp', 'feb'), monNum('inp', 'march'), monNum('inp', 'april'), monNum('inp', 'may')
      , monNum('inp', 'june'), monNum('inp', 'july'), monNum('inp', 'aug'), monNum('inp', 'sep'), monNum('inp', 'oct')
      , monNum('inp', 'nov'), monNum('inp', 'dec')],
  },

  {
    label: 'Offers',
    backgroundColor: 'rgba(255, 165, 0, 0.2)',
    borderColor: 'rgba(255, 165, 0, 1)',
    borderWidth: 1,
    data: [monNum('off', 'jan'), monNum('off', 'feb'), monNum('off', 'march'), monNum('off', 'april'), monNum('off', 'may')
      , monNum('off', 'june'), monNum('off', 'july'), monNum('off', 'aug'), monNum('off', 'sep'), monNum('off', 'oct')
      , monNum('off', 'nov'), monNum('off', 'dec')],
  }]
};

// Configuration options
const config = {
  type: 'bar',
  data: data,
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          precision: 0,
        },
      },
    },
  },
};

// Create chart
const ctx = document.getElementById('job-applications-chart').getContext('2d');
const chart = new Chart(ctx, config);
cmonth('wish')
cmonth('inp')
cmonth('app')
cmonth('off')
