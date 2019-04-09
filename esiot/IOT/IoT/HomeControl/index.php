<!DOCTYPE html>
<?php

        $op = $_GET['op'];

	    shell_exec("/usr/local/bin/gpio -g mode 7 out");	#Latch
		shell_exec("/usr/local/bin/gpio -g mode 12 out");	#Light
		shell_exec("/usr/local/bin/gpio -g mode 16 out");	#FAN1
		shell_exec("/usr/local/bin/gpio -g mode 6 out");	#Buzzer
		
		shell_exec("/usr/local/bin/gpio -g write 7 0");
        shell_exec("/usr/local/bin/gpio -g write 12 0");
        shell_exec("/usr/local/bin/gpio -g write 16 0");
		shell_exec("/usr/local/bin/gpio -g write 6 1");

        switch($op){
				case 1: shell_exec("/usr/local/bin/gpio -g write 7 0");#Door Latch OFF
                        break;
                case 2: shell_exec("/usr/local/bin/gpio -g write 7 1");#Door Latch ON
                        break;
                case 3: shell_exec("/usr/local/bin/gpio -g write 12 0");#Light 1
                        break;
                case 4: shell_exec("/usr/local/bin/gpio -g write 12 1");
                        break;
                case 5: shell_exec("/usr/local/bin/gpio -g write 16 0");#FAN1
                        break;
                case 6: shell_exec("/usr/local/bin/gpio -g write 16 1");
                        break;
                case 7: shell_exec("/usr/local/bin/gpio -g write 6 1");#Buzzer
                        break;
				case 8: shell_exec("/usr/local/bin/gpio -g write 6 0");
                        break;	
				case 9:	shell_exec("/usr/local/bin/gpio -g write 7 0");
                        shell_exec("/usr/local/bin/gpio -g write 12 0");
                        shell_exec("/usr/local/bin/gpio -g write 16 0");
						shell_exec("/usr/local/bin/gpio -g write 6 1");	
						break;	
 				
        }
        include("page.html");
?>