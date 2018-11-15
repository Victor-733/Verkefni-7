<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Page Title</title>
    <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
</head>
<body>
    <h2>Félagskrá</h2>
    <p>the member team are as follows:</p>
    <table border="1">
    % for row in rows:
    <tr>
        % for col in row:
            <td>{{col}}</td>
        % end
    </tr>
    % end
    </table>
    <a href="/">Aftur á heimasíðu</a>
</body>
</html>