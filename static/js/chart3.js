//Se ejecuta cuando cargue todo el html
$(document).ready(function() {

	//var ctx1 = $("#chart1");
    //var chart1 = new Chart (ctx1, settings1);

    
   

    //var ctx3 = $("#chart3");
	//var chart3 = new Chart (ctx3, settings3);

    //var ctx4 = $("#chart4");
    //var chart3 = new Chart (ctx4, settings4);

    var ctx5 = $("#chart5");
    var mixedChart = new Chart(ctx5, settings5);

    var ctx6 = $("#chart6");
    var chart6 = new Chart(ctx6, settings6);
});

  document.addEventListener("DOMContentLoaded", function(event) {
    console.log("DOM fully loaded and parsed");var x = window.matchMedia("(max-height: 650px)")
if(x.matches){Chart.defaults.global.legend.position = 'right';Chart.defaults.global.maintainAspectRatio = true;Chart.defaults.global.defaultFontColor = 'white';}
else{Chart.defaults.global.legend.position = 'bottom';Chart.defaults.global.maintainAspectRatio = false;Chart.defaults.global.defaultFontColor = 'white';}
  });

//Esto se ejecuta cuando llegue a la linea del html que carga este script
var endpoint = '/data'
$.ajax({
    method: 'GET',
    url: endpoint,
    success: function(data){
        //alertas
        var ctx1 = $("#chart1");
        var settings1 = {
                type: 'doughnut',
                data: {
        labels: data.data1.labels1,
                    datasets: [{
            data: data.data1.data1,
                        backgroundColor: [
                            'rgba(148, 49, 38, 1)',
                            'rgba(176, 58, 46, 1)',
                            'rgba(203, 67, 53, 1)',
                            'rgba(231, 76, 60, 1)'
                        ],   
                    }]
                },

                options: {
                responsive: true,
                
                    legend: {
                        
                        labels: {
                            fontColor: '#fff',
                            boxWidth: 15,
                            padding: 15,
                            fontSize: 11
                        }
                    }

                }
            };
        var chart1 = new Chart (ctx1, settings1);

        //ip origen  
        var ctx4 = $("#chart4");
        var settings4 = {
        type: 'doughnut',
        data: {
        labels: data.data4.labels4,
        datasets: [{
            data: data.data4.data4,
            backgroundColor: [
                'rgba(24, 106, 59, 1)',
                'rgba(35, 155, 86, 1)',
                'rgba(40, 180, 99, 1)',
                'rgba(29, 131, 72, 1)'
                      ],   
                    }]
                },

                options: {
                responsive: true,
                
                    legend: {
                        
                        labels: {
                            fontColor: '#fff',
                            boxWidth: 15,
                            padding: 15,
                            fontSize: 11
                        }
                    }

                }
            };
        var chart4 = new Chart (ctx4, settings4);

        //ip destino
        var ctx3 = $("#chart3");
        var settings3 = {
            type: 'doughnut',
            data: {
                labels: data.data3.labels3,
                datasets: [{
                    data: data.data3.data3,
            backgroundColor: [
                'rgba(24, 106, 59, 1)',
                'rgba(35, 155, 86, 1)',
                'rgba(40, 180, 99, 1)',
                'rgba(29, 131, 72, 1)'
                      ],   
                    }]
                },

                options: {
                responsive: true,
                
                    legend: {
                        
                        labels: {
                            fontColor: '#fff',
                            boxWidth: 15,
                            padding: 15,
                            fontSize: 11
                        }
                    }

                }
            };
            var chart3 = new Chart (ctx3, settings3);

            //riesgo
            var ctx2 = $("#chart2");
            var settings2 = {
            type: 'doughnut',
             data: {
             labels: data.data2.labels2,
                datasets: [{
                   data: data.data2.data2,
                 backgroundColor: [
                  'rgba(148, 49, 38, 1)',
                  'rgba(176, 58, 46, 1)',
                  'rgba(203, 67, 53, 1)',
                  'rgba(231, 76, 60, 1)'
                       ],   
                    }]
                },

                options: {
                responsive: true,
                
                    legend: {
                        
                        labels: {
                            fontColor: '#fff',
                            boxWidth: 15,
                            padding: 15,
                            fontSize: 11
                        }
                    }

                }
            };
            var chart2 = new Chart (ctx2, settings2);


    }


});


var settings2 = {
    type: 'doughnut',
    data: {
        labels: ['Smartphone', 'Server', 'BBDD', 'Pc'],
        datasets: [{
            data: [12, 19, 3, 5],
            backgroundColor: [
                  'rgba(148, 49, 38, 1)',
                  'rgba(176, 58, 46, 1)',
                  'rgba(203, 67, 53, 1)',
                  'rgba(231, 76, 60, 1)'
                       ],   
                    }]
                },

                options: {
                responsive: true,
                
                    legend: {
                        
                        labels: {
                            fontColor: '#fff',
                            boxWidth: 15,
                            padding: 15,
                            fontSize: 11
                        }
                    }

                }
            };






var settings5 = {
    type: 'bar',
    data: {
        datasets: [{
            label: 'Trafico total (TBs/dia)',
            data: [10, 20, 30, 40, 60, 25, 36, 78, 20, 30, 40,60,25,36,78],
            backgroundColor: [
                'rgba(24, 106, 59, 1)',
                'rgba(35, 155, 86, 1)',
                'rgba(40, 180, 99, 1)',
                'rgba(29, 131, 72, 1)',
                'rgba(24, 106, 59, 1)',
                'rgba(35, 155, 86, 1)',
                'rgba(40, 180, 99, 1)',
                'rgba(29, 131, 72, 1)',
                'rgba(24, 106, 59, 1)',
                'rgba(35, 155, 86, 1)',
                'rgba(40, 180, 99, 1)',
                'rgba(29, 131, 72, 1)',
                 'rgba(24, 106, 59, 1)',
                'rgba(35, 155, 86, 1)',
                'rgba(40, 180, 99, 1)'
                        ],
            borderWidth: 2,
            borderColor: [
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)'],

                order: 2
        }, {
            label: 'Amenazas',
            data: [14, 8, 9, 3, 14, 8, 9, 14, 8, 9, 3, 14, 8, 9, 3],
            backgroundColor: [
                'rgba(0, 0, 0, 0)'
            ],
            borderColor: ['rgba(192, 57, 43, 1)'],
            borderJoinStyle: 'mitle',
            borderCapStyle: 'butt',

            // Changes this dataset to become a line
            type: 'line',
            order: 1
        }],
        labels: ['L 2', 'M 3', 'M 4', 'J 5', 'V 6', 'S 7', 'D 8', 'L 9', 'M 10', 'M 11', 'J 12', 'V 13', 'S 14', 'D 15', 'L 16']
    },
     options: {
                responsive: true,
                
                    legend: {
                        position: 'bottom',
                        labels: {
                            fontColor: '#fff',
                            boxWidth: 15,
                            padding: 15,
                            fontSize: 11
                        }
                    }

                }

}

var settings6 = {
    type: 'line',
  data: {
    labels: ['L 2', 'M 3', 'M 4', 'J 5', 'V 6', 'S 7', 'D 8', 'L 9', 'M 10', 'M 11', 'J 12', 'V 13', 'S 14', 'D 15', 'L 16'],
    datasets: [{ 
        data: [14, 8, 9, 3, 14, 8, 9, 14, 8, 9, 3, 14, 8, 9, 3],
        label: "Amenazas",
        backgroundColor: [
                'rgba(175,1,1,0.5)'
                        ],
        borderColor: ['rgba(180, 1, 1, 0.8)'],
        fill: true,
        },  
    ]
  },
  options: {

    title: {
      display: true,
      text: 'Amenazas detectadas por dia',
      fontColor: '#fff',
    }



  }
};
