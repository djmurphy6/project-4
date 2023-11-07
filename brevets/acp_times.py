"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow, math

#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """

    start = arrow.get(brevet_start_time)

    num = control_dist_km
    sum = 0.0
    if num > 600 and num <= 1000:
       sum += ((num-600)/28)
       num = 600
    if num > 400 and num <= 600:
       sum += ((num-400)/30)
       num = 400
    if num > 200 and num <= 400:
       sum += ((num-200)/32)
       num = 200
    if num > 0 and num <= 200:
       sum += ((num)/34)
    
    hrs = math.floor(sum)
    min = int(round((sum - math.floor(sum))*60, 0))
   
    return start.shift(hours=+hrs, minutes =+ min)


   
   # outline
   # if distance is 0-200, max speed is 34 km/h
         # so, distance/34 is the time
   # if distance 200-400, max speed is 32
            # greater than 200 so do 200/34 + (distance-200)/32
   # if distance 400-600 max is 30
            # time for first 200 +time for 




def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    close = arrow.get(brevet_start_time)

    num = control_dist_km
    sum = 0.0
    if num < 60:
       sum = (num/20) + 1
    else:
      if num > 600 and num <= 1000:
         sum += ((num-600)/11.428)
         num = 600
      if num > 0 and num <= 600:
         sum += (num/15)
      if num == 0:
         sum = 1
    
    hrs = math.floor(sum)
    min = int(round((sum - math.floor(sum))*60, 0))

    return close.shift(hours =+ hrs, minutes =+ min)
