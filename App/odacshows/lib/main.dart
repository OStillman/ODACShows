import 'package:flutter/material.dart';
import 'on_demand/on_demand_entry.dart';

import 'helpers/constants.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ODAC Shows',
      theme: ThemeData(
        primaryColor: Colors.cyan[900],
        accentColor: Colors.cyan,
        primaryColorDark: Colors.teal[800],
        primaryColorLight: Colors.teal[100],
      ),
      //home: MyHomePage(),
      initialRoute: '/',
      routes: {
        '/': (context) => MyHomePage(),
        '/OD': (context) => OnDemandEntry(),
      },
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey[800],
      appBar: AppBar(
        title: Text("ODAC Shows"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: <Widget>[
            Text(
              "Welcome to ODAC Shows!",
              style: TextStyle(fontSize: 40, color: Colors.white),
              textAlign: TextAlign.center,
            ),
            Container(
              child: Column(
                children: <Widget>[
                  ElevatedButton(
                      onPressed: () {
                        Navigator.pushNamed(context, '/OD');
                      },
                      style: ButtonStyle(
                          backgroundColor:
                              MaterialStateProperty.all(Colors.cyan),
                          fixedSize:
                              MaterialStateProperty.all(Size(150.0, 100.0))),
                      child: const Text(
                        "On Demand Shows",
                        style: TextStyle(color: Colors.white, fontSize: 20.0),
                        textAlign: TextAlign.center,
                      )),
                  Padding(
                    padding: EdgeInsets.only(top: 5),
                    child: ElevatedButton(
                        onPressed: null,
                        style: ButtonStyle(
                            backgroundColor:
                                MaterialStateProperty.all(Colors.cyan),
                            fixedSize:
                                MaterialStateProperty.all(Size(150.0, 100.0))),
                        child: const Text(
                          "Live Shows",
                          style: TextStyle(color: Colors.white, fontSize: 20.0),
                          textAlign: TextAlign.center,
                        )),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
