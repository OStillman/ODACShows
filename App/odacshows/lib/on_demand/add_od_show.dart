import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import '/helpers/constants.dart';

import 'package:flutter/material.dart';
import '/on_demand/on_demand_entry.dart';

import '/helpers/constants.dart';

import 'workers/add_od_show_worker.dart';

class AddODShow extends StatefulWidget {
  @override
  _AddODShow createState() => _AddODShow();
}

class _AddODShow extends State<AddODShow> {
  int _index = 0;
  bool _watching = false;
  bool _missing_input = false;
  final TextEditingController _show_name_controller = TextEditingController();
  final TextEditingController _show_series_controller = TextEditingController();
  final TextEditingController _show_episode_controller =
      TextEditingController();
  String? _show_name;
  String? _show_series;
  String? _show_episode;
  String? _watching_ui = "No";
  List<bool> _completion = [false, false, false, true];
  List<String> _default_values = ["Show?", "?", "?", "?"];

  @override
  void initState() {
    super.initState();

    _show_name_controller.addListener(() {
      final String text = _show_name_controller.text;
      _show_name_controller.value = _show_name_controller.value.copyWith(
        text: text,
      );
      _show_name_controller.selection = TextSelection.fromPosition(
          TextPosition(offset: _show_name_controller.text.length));
    });

    _show_series_controller.addListener(() {
      final String number = _show_series_controller.text;
      _show_series_controller.value = _show_series_controller.value.copyWith(
        text: number,
      );
      _show_series_controller.selection = TextSelection.fromPosition(
          TextPosition(offset: _show_series_controller.text.length));
    });

    _show_episode_controller.addListener(() {
      final String number = _show_episode_controller.text;
      _show_episode_controller.value = _show_episode_controller.value.copyWith(
        text: number,
      );
      _show_episode_controller.selection = TextSelection.fromPosition(
          TextPosition(offset: _show_episode_controller.text.length));
    });
  }

  @override
  void dispose() {
    _show_name_controller.dispose();
    _show_series_controller.dispose();
    _show_episode_controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey[800],
      appBar: AppBar(
        title: Text("New On Demand Show"),
      ),
      body: Stepper(
        currentStep: _index,
        controlsBuilder: (BuildContext context,
            {VoidCallback? onStepContinue, VoidCallback? onStepCancel}) {
          return Row(
            children: <Widget>[
              ElevatedButton(
                  onPressed: onStepContinue,
                  child: const Text('NEXT'),
                  style: ElevatedButton.styleFrom(primary: Colors.cyan)),
              Padding(padding: EdgeInsets.all(10)),
              ElevatedButton(
                  onPressed: onStepCancel,
                  child: const Text(
                    'BACK',
                    style: TextStyle(color: Colors.white),
                  ),
                  style: ElevatedButton.styleFrom(primary: Colors.cyan)),
            ],
          );
        },
        onStepCancel: () {
          if (_index > 0) {
            setState(() {
              _index -= 1;
            });
          }
        },
        onStepContinue: () {
          if (_index <= 2) {
            updateWidgets();
            setState(() {
              _index += 1;
            });
          } else {
            List<dynamic> _completion_check = _completionChecker();
            if (_completion_check[0] == false){
              ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(
                  content: Text("You've Missed " + _completion_check[1]),
                ),
              );
            }
            else{
              showDialog<String>(
                context: context,
                builder: (BuildContext context) => AlertDialog(
                  title: const Text('Show Added!'),
                  content: const Text('Great! Your On Demand Show has been successfully added'),
                  actions: <Widget>[
                    TextButton(
                      onPressed: () => Navigator.popUntil(context, ModalRoute.withName('/OD')),
                      child: const Text('OK'),
                    ),
                  ],
                ),
              );
            }
          }
        },
        onStepTapped: (int index) {
          updateWidgets();
          setState(() {
            _index = index;
          });
        },
        steps: <Step>[
          Step(
            state: _getStepState(0),
            title: const Text(
              'Add Your Show Name:',
              style: TextStyle(color: Colors.white),
            ),
            subtitle: Text(_textOutput(_show_name, _default_values[0]),
                style: TextStyle(color: Colors.white)),
            content: Container(
                alignment: Alignment.centerLeft,
                child: TextFormField(
                  textCapitalization: TextCapitalization.words,
                  controller: _show_name_controller,
                  decoration: const InputDecoration(
                      fillColor: Colors.white, filled: true),
                )),
          ),
          Step(
            state: _getStepState(1),
            title: Text('Add Current Series:',
                style: TextStyle(color: Colors.white)),
            subtitle: Text(
                'Series ' + _textOutput(_show_series, _default_values[1]),
                style: TextStyle(color: Colors.white)),
            content: Container(
                alignment: Alignment.centerLeft,
                child: TextFormField(
                  decoration: const InputDecoration(
                      fillColor: Colors.white, filled: true),
                  keyboardType: TextInputType.number,
                  maxLength: 2,
                  controller: _show_series_controller,
                )),
          ),
          Step(
            state: _getStepState(2),
            title: Text('Add Current Episode:',
                style: TextStyle(color: Colors.white)),
            subtitle: Text(
                'Episode ' + _textOutput(_show_episode, _default_values[2]),
                style: TextStyle(color: Colors.white)),
            content: Container(
                alignment: Alignment.centerLeft,
                child: TextFormField(
                  decoration: const InputDecoration(
                      fillColor: Colors.white, filled: true),
                  keyboardType: TextInputType.number,
                  maxLength: 3,
                  controller: _show_episode_controller,
                )),
          ),
          Step(
            state: _getStepState(3),
            title: Text('Are you Currently Watching this Show?',
                style: TextStyle(color: Colors.white)),
            subtitle: Text(
                'Watching: ' + _textOutput(_watching_ui, _default_values[3]),
                style: TextStyle(color: Colors.white)),
            content: Container(
              alignment: Alignment.centerLeft,
              child: Switch(
                value: _watching,
                onChanged: _watchingChange,
              ),
            ),
          ),
        ],
      ),
    );
  }

  StepState _getStepState(index) {
    if (_completion[index]) {
      return StepState.complete;
    } else {
      return StepState.error;
    }
  }

  void updateWidgets() {
    switch (_index) {
      case 0:
        {
          _show_name = _checkInput(_show_name_controller.text, _index);
        }
        break;
      case 1:
        {
          _show_series = _checkInput(_show_series_controller.text, _index);
        }
        break;
      case 2:
        {
          _show_episode = _checkInput(_show_episode_controller.text, _index);
        }
        break;
      case 3:
        {
          _watching_ui = _watchingUIController(_index);
        }
        break;
    }
  }

  String? _checkInput(String input, int index) {
    if (input.length == 0) {
      _completion[index] = false;
      return null;
    } else {
      _completion[index] = true;
      return input;
    }
  }

  String _watchingUIController(int index) {
    if (_watching) {
      _completion[index] = true;
      return "Yes";
    } else {
      _completion[index] = true;
      return "No";
    }
  }

  void _watchingChange(status) {
    _watching = status;
    _watching_ui = _watchingUIController(3);
    setState(() {});
  }

  String _textOutput(current_value, default_value) {
    if (current_value == null) {
      return default_value;
    } else {
      return current_value;
    }
  }

  List<dynamic> _completionChecker() {
    SendODShow sendODShow = SendODShow(
        show_name: _show_name,
        current_episode: _show_episode,
        current_series: _show_series,
        watching: _watching);
    List<dynamic> _outcome = sendODShow.checkValuesExist();
    print(_outcome);
    if (_outcome[0]){
      //Run the Add Script
    }
    return _outcome;
  }
}
