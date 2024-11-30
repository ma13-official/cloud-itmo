<?php

$conn = new mysqli("mysql", "dshevelev", "1234", "cloud_lab3");

if ($conn->connect_error) {
    die("Ошибка подключения к базе данных");
}

$data = $conn->query("SELECT * FROM test");

if ($data->num_rows == 0) {
    $conn->close();
    die("Нет ни одной записи в таблице");
}

$first_row = $data->fetch_assoc();
echo "Первая строка - id записи: " . $first_row["id"] . ", текст: " . $first_row["text"];
$conn->close();

?>