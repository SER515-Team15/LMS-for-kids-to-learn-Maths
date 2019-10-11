<?php
print_r($_REQUEST['addmore']);
print_r($_REQUEST['addmore1']);
$Question_values_array = $_POST['addmore1'];
foreach($Question_values_array as $value){
    //database query
}
print_r($Question_values_array);
$Answer_values_array = $_POST['addmore'];
foreach($Answer_values_array as $value){
    // database query
}
print_r($Answer_values_array);
exit;
?>