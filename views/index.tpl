<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Skráning</title>
    <link rel="stylesheet" type="text/css" media="screen" href="/static/styles.css" />
</head>
<body>
    <h3>Nýskráningarform</h3><br>
    <form action="/donyskra" method="post", accept-charset="ISO-8859-1", id="ny">
        Notendanafn: <br>
        <input type="text", name="user"> <br>
        Lykilorð: <br>
        <input type="password", name="pass"> <br>
        Nafn: <br>
        <input type="text" name="nafn" required><br>
        <input type="submit" value="Nýskrá">
        <input type="reset" value="Hreinsa">
    </form>
    <hr>
    <h3>Innskráningarform</h3><br>
    <form action="/doinnskra" method="post" accept-charset="ISO-8859-1", id="inn">
        Notendanafn: <br>
        <input type="text", name="user", required><br>
        Lykilorð: <br>
        <input type="password", name="pass", required><br>
        <input type="submit" value="Nýskrá">
        <input type="reset" value="Hreinsa">
    </form>
</body>
</html>