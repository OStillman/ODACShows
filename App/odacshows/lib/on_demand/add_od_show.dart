import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import '/helpers/constants.dart';

import 'package:flutter/material.dart';
import '/on_demand/on_demand_entry.dart';

import '/helpers/constants.dart';

class AddODShow extends StatefulWidget {
  @override
  _AddODShow createState() => _AddODShow();
}

class _AddODShow extends State<AddODShow> {
  int _index = 0;
  bool _watching = false;
  final TextEditingController _show_name_controller = TextEditingController();
  final TextEditingController _show_series_controller = TextEditingController();
  final TextEditingController _show_episode_controller = TextEditingController();
  String _show_name = "Show?";
  String _show_series = "?";
  String _show_episode = "?";
  String _watching_ui = "No";
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
            subtitle: Text(_show_name, style: TextStyle(color: Colors.white)),
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
            subtitle: Text('Series $_show_series',
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
            subtitle: Text('Episode $_show_episode', style: TextStyle(color: Colors.white)),
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
            subtitle:
                Text('Watching: $_watching_ui', style: TextStyle(color: Colors.white)),
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

  String _checkInput(String input, int index) {
    if (input.length == 0) {
      _completion[index] = false;
      return _default_values[index];
    } else {
      _completion[index] = true;
      return input;
    }
  }

  String _watchingUIController(int index){
    if (_watching){
      _completion[index] = true;
      return "Yes";
    }
    else{
      _completion[index] = true;
      return "No";
    }
  }

  void _watchingChange(status) {
    _watching = status;
    _watching_ui = _watchingUIController(3);
    setState(() {});
  }
}
