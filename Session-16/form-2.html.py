<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>FORM 2</title>
  </head>
  <body>
    <h3>Example of different input elements</h3>

    <form action="myserver" method="get">
      Text input  <input type="text" name="msg">
      <br><br>
      Check button:
      <input type="checkbox" name="chk">
      <br><br>
      Radio buttons:
      <input type="radio" name="base" value="A" checked> A
      <input type="radio" name="base" value="C"> C
      <input type="radio" name="base" value="T"> T
      <input type="radio" name="base" value="G"> G
      <br><br>
      Options: <br>
      Choose operation:
      <select name="operation">
        <option value="count">Count</option>
        <option value="perc">Percentage</option>
      </select>
       <br>
        <input type="submit"/>
    </form>

  </body>
</html>