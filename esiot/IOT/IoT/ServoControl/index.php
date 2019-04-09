<!DOCTYPE html>
<?php

        $op = $_GET['op'];

	    shell_exec("/usr/local/bin/gpio mode 1 pwm");	#servo
		shell_exec("/usr/local/bin/gpio pwm-ms");		#servo
		shell_exec("/usr/local/bin/gpio pwmc 1920");	#set pwm clock to 1920 :50 Hz 
		shell_exec("/usr/local/bin/gpio pwmr 200");		#set pwm range to 200
		shell_exec("/usr/local/bin/gpio pwm 1 15");		#set centre position
		
		


        switch($op){
				case 1: shell_exec("/usr/local/bin/gpio pwm 1 24");#left
                        break; 
                case 2: shell_exec("/usr/local/bin/gpio pwm 1 15");#centre
                        break;
                case 3: shell_exec("/usr/local/bin/gpio pwm 1 6");#right
                        break;
				case 4:	shell_exec("/usr/local/bin/gpio pwm 1 6");
						shell_exec("sleep(1)");
						shell_exec("/usr/local/bin/gpio pwm 1 8");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 10");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 12");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 14");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 16");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 18");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 10");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 22");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 24");
						shell_exec("sleep(0.5)");
						break;
				case 5: shell_exec("/usr/local/bin/gpio pwm 1 24");
						shell_exec("sleep(1)");
						shell_exec("/usr/local/bin/gpio pwm 1 22");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 20");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 18");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 16");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 14");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 12");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 10");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 8");
						shell_exec("sleep(0.5)");
						shell_exec("/usr/local/bin/gpio pwm 1 6");
						shell_exec("sleep(0.5)");
						break;
				case 6:
						shell_exec("/usr/local/bin/gpio -g mode 18 out");
						shell_exec("/usr/local/bin/gpio -g write 18 0");
						break;
        }
        include("page.html");
?>