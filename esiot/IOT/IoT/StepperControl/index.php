<!DOCTYPE html>
<?php

        $op = $_GET['op'];

	    shell_exec("/usr/local/bin/gpio -g mode 22 out");
		shell_exec("/usr/local/bin/gpio -g mode 23 out");
		shell_exec("/usr/local/bin/gpio -g mode 24 out");
		shell_exec("/usr/local/bin/gpio -g mode 25 out");
		
		
        switch($op){
				case 1: 
						for($count=0;$count<=50;$count++)
						{
							shell_exec("/usr/local/bin/gpio -g write 22 0");
							shell_exec("/usr/local/bin/gpio -g write 23 1");
							shell_exec("/usr/local/bin/gpio -g write 24 1");
							shell_exec("/usr/local/bin/gpio -g write 25 1");
							
							shell_exec("/usr/local/bin/gpio -g write 22 0");
							shell_exec("/usr/local/bin/gpio -g write 23 0");
							shell_exec("/usr/local/bin/gpio -g write 24 1");
							shell_exec("/usr/local/bin/gpio -g write 25 1");
							
							shell_exec("/usr/local/bin/gpio -g write 22 1");
							shell_exec("/usr/local/bin/gpio -g write 23 0");
							shell_exec("/usr/local/bin/gpio -g write 24 1");
							shell_exec("/usr/local/bin/gpio -g write 25 1");
							
							shell_exec("/usr/local/bin/gpio -g write 22 1");
							shell_exec("/usr/local/bin/gpio -g write 23 0");
							shell_exec("/usr/local/bin/gpio -g write 24 0");
							shell_exec("/usr/local/bin/gpio -g write 25 1");
							
							shell_exec("/usr/local/bin/gpio -g write 22 1");
							shell_exec("/usr/local/bin/gpio -g write 23 1");
							shell_exec("/usr/local/bin/gpio -g write 24 0");
							shell_exec("/usr/local/bin/gpio -g write 25 1");
							
							shell_exec("/usr/local/bin/gpio -g write 22 1");
							shell_exec("/usr/local/bin/gpio -g write 23 1");
							shell_exec("/usr/local/bin/gpio -g write 24 0");
							shell_exec("/usr/local/bin/gpio -g write 25 0");
							
							shell_exec("/usr/local/bin/gpio -g write 22 1");
							shell_exec("/usr/local/bin/gpio -g write 23 1");
							shell_exec("/usr/local/bin/gpio -g write 24 1");
							shell_exec("/usr/local/bin/gpio -g write 25 0");
							
							shell_exec("/usr/local/bin/gpio -g write 22 0");
							shell_exec("/usr/local/bin/gpio -g write 23 1");
							shell_exec("/usr/local/bin/gpio -g write 24 1");
							shell_exec("/usr/local/bin/gpio -g write 25 0");
							
						}
                        break; 
                
				case 2:	
						for($count=0;$count<=50;$count++)
						{
							shell_exec("/usr/local/bin/gpio -g write 22 0");
							shell_exec("/usr/local/bin/gpio -g write 23 1");
							shell_exec("/usr/local/bin/gpio -g write 24 1");
							shell_exec("/usr/local/bin/gpio -g write 25 0");
							
							shell_exec("/usr/local/bin/gpio -g write 22 1");
							shell_exec("/usr/local/bin/gpio -g write 23 1");
							shell_exec("/usr/local/bin/gpio -g write 24 1");
							shell_exec("/usr/local/bin/gpio -g write 25 0");
							
							shell_exec("/usr/local/bin/gpio -g write 22 1");
							shell_exec("/usr/local/bin/gpio -g write 23 1");
							shell_exec("/usr/local/bin/gpio -g write 24 0");
							shell_exec("/usr/local/bin/gpio -g write 25 0");
							
							shell_exec("/usr/local/bin/gpio -g write 22 1");
							shell_exec("/usr/local/bin/gpio -g write 23 1");
							shell_exec("/usr/local/bin/gpio -g write 24 0");
							shell_exec("/usr/local/bin/gpio -g write 25 1");
							
							shell_exec("/usr/local/bin/gpio -g write 22 1");
							shell_exec("/usr/local/bin/gpio -g write 23 0");
							shell_exec("/usr/local/bin/gpio -g write 24 0");
							shell_exec("/usr/local/bin/gpio -g write 25 1");
							
							shell_exec("/usr/local/bin/gpio -g write 22 1");
							shell_exec("/usr/local/bin/gpio -g write 23 0");
							shell_exec("/usr/local/bin/gpio -g write 24 1");
							shell_exec("/usr/local/bin/gpio -g write 25 1");
							
							shell_exec("/usr/local/bin/gpio -g write 22 0");
							shell_exec("/usr/local/bin/gpio -g write 23 0");
							shell_exec("/usr/local/bin/gpio -g write 24 1");
							shell_exec("/usr/local/bin/gpio -g write 25 1");
							
							shell_exec("/usr/local/bin/gpio -g write 22 0");
							shell_exec("/usr/local/bin/gpio -g write 23 1");
							shell_exec("/usr/local/bin/gpio -g write 24 1");
							shell_exec("/usr/local/bin/gpio -g write 25 1");
							
							
						}
						break;
				case 3:
						{
							shell_exec("/usr/local/bin/gpio -g write 22 1");
							shell_exec("/usr/local/bin/gpio -g write 23 1");
							shell_exec("/usr/local/bin/gpio -g write 24 1");
							shell_exec("/usr/local/bin/gpio -g write 25 1");		
						break;	
						}
						

        }
				 
        include("page.html");
?>