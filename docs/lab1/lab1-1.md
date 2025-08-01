# Connection Strings
Whether your are using the mongosh command line, the Compass GUI, or one of
the many [drivers](https://www.mongodb.com/docs/drivers/) available for your
programming language of choice, you will use a 
[connection string](https://www.mongodb.com/docs/manual/reference/connection-string/)
to tell your application how to find your cluster members, what credentials
to you, and other paramaters to establish that initial connection.

## Elements of a connection string

<h5><span style="color:#1c00ff">mongodb+srv</span>://<span style="color:#ff0000">myDatabaseUser:D1fficultP%40ssw0rd</span>@<span style="color:#04a200">mongodb0.example.com</span>/?<span style="color:#be7100">authSource=admin&replicaSet=myRepl</span></h5>

- <span style="color:#1c00ff">mongodb+srv</span>: The type of connection string.
- <span style="color:#ff0000">myDatabaseUser:D1fficultP%40ssw0rd</span>: The
  credentials for the cluster.
- <span style="color:#04a200">mongodb0.example.com</span>: The hostname for
  the cluster.
- <span style="color:#be7100">authSource=admin&replicaSet=myRepl</span>: 
  Additional options for this connection.

# Lab: Finding your connection string
1. In your jumphost, double-click the `Atlas Connection String.txt` icon on your
desktop.

![Image of the connection string file on the desktop](images/connection-string-icon.png)

2. This will open a file containing the connection string for your personal
MongoDB Atlas lab cluster.

![Image of the contents of the connection string file](images/connection-string-file.png)

> 👆 **Note**: Keep this string handy. It's for your own personal MongoDB Atlas
> lab cluster, and you will be using it during the rest of the labs.