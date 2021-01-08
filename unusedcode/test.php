<?php
$old_path = getcwd();
chdir('/home/sean/Desktop/ResumeWriter/');
shell_exec('./RUNME.sh https://www.internsg.com/job/singapore-lactation-bakes-marketing-communication-intern/');
chdir($old_path);
?>
