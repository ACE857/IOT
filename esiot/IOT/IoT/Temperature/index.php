<?php

$page = $_SERVER['PHP_SELF'];
$temp = file_get_contents('ds18b20.txt');
echo "Please run the python script for the temperature sensor<br>";
echo "Use the following command: sudo python tempServer.py<br><br>";
echo "DS18B20 Sensor Output: ";
header("Refresh: 2; url=$page");
echo $temp." degree Celcius";

?>
