Author: Dylan Murphy

Contact: dmurphy6@uoregon.edu

Description: This is a checkpoint calculator for brevet bike races. It follows the table: 
| Control Location (km) | Minimum Speed (km/hr) | Maximum Speed (km/hr) |
|-----------------------|-----------------------|-----------------------|
| 0 - 200               | 15                    | 34                    |
| 200 - 400             | 15                    | 32                    |
| 400 - 600             | 15                    | 30                    |
| 600 - 1000            | 11.428                | 28                    |

and has a special case for checkpoints within the first 60km where the close time is a 20 km/hr minimum speed + 1 hr. The maximum distance for the last checkpoint is 120% the brevet distance and if you type in a number that exceeds that it will automatically default to 120% * the brevet distance. The page updates as you type in values without reloading the page by using AJAX. 

To run this, get in the "brevet" directory and run the following commands:

$ docker build -t <image_name> .
$ docker run -d -p 5001:<port number in credentials.ini file> <image_name>

the -d flag detaches it so that your terminal does not get filled up
the -p flag is what allows you to designate the port

now, go to your preferred web browser and type:

localhost:5001

into the search bar. Now you are ready to start entering values.
