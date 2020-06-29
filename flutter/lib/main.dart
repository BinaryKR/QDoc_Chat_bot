// ignore: avoid_web_libraries_in_flutter

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_custom_tabs/flutter_custom_tabs.dart';
import 'package:flutter_inappwebview/flutter_inappwebview.dart';
import 'package:flutter_polyline_points/flutter_polyline_points.dart';
import 'package:flutter_webview_plugin/flutter_webview_plugin.dart';

import 'package:fluttertoast/fluttertoast.dart';
import 'package:geolocator/geolocator.dart';
import 'package:google_map_polyline/google_map_polyline.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:medicinereminder/animations/fade_animation.dart';
import 'package:medicinereminder/enums/icon_enum.dart';
import 'package:medicinereminder/models/Medicine.dart';
import 'package:medicinereminder/widgets/AddMedicine.dart';
import 'package:medicinereminder/widgets/AppBar.dart';
import 'package:medicinereminder/widgets/DeleteIcon.dart';
import 'package:medicinereminder/widgets/MedicineEmptyState.dart';
import 'package:medicinereminder/widgets/MedicineGridView.dart';
import 'package:permission/permission.dart';
import 'package:provider/provider.dart';
import 'package:scoped_model/scoped_model.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:webview_flutter/webview_flutter.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'dart:async';

import 'helper.dart';
import 'inherited_manga.dart';
import 'manga.dart';
import 'map_request.dart';
import 'search_manga.dart';

void main() {
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    title: '충무로클라쓰',
    home: First(),
  ));
}

class First extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Qdoc')),
      body: Stack(
        children: <Widget>[
          Center(
            child: new Image.asset(
              'assets/background.png',
              fit: BoxFit.fill,
            ),
          ),
          GridView.count(
            crossAxisCount: 2,
            childAspectRatio: 4.0 / 2.9,
            children: <Widget>[
              Row(
                children: <Widget>[],
              ),
              Row(
                children: <Widget>[],
              ),
              Row(
                children: <Widget>[],
              ),
              Row(
                children: <Widget>[],
              ),
              Row(
                children: <Widget>[],
              ),
              Row(
                children: <Widget>[],
              ),
              Row(
                children: <Widget>[
                  InkWell(
                    child: Image.asset('assets/Clear_Button.png',
                        width: 100, height: 100),
                    onTap: () {
                      Navigator.push(context, MaterialPageRoute<void>(
                          builder: (BuildContext context) {
                        return WebViewExample();
                      }));
                    },
                  ),
                ],
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
              ),
              Row(
                children: <Widget>[
                  InkWell(
                    child: Image.asset('assets/Clear_Button.png',
                        width: 100, height: 100),
                    onTap: () {
                      Navigator.push(context, MaterialPageRoute<void>(
                          builder: (BuildContext context) {
                        return MediDic();
                      }));
                    },
                  ),
                ],
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
              ),
              Row(
                children: <Widget>[
                  InkWell(
                    child: Image.asset('assets/Clear_Button.png',
                        width: 100, height: 100),
                    onTap: () {
                      Navigator.push(context, MaterialPageRoute<void>(
                          builder: (BuildContext context) {
                        return Alarm();
                      }));
                    },
                  ),
                ],
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
              ),
              Row(
                children: <Widget>[
                  InkWell(
                    child: Image.asset('assets/Clear_Button.png',
                        width: 100, height: 100),
                    onTap: () {
                      Navigator.push(context, MaterialPageRoute<void>(
                          builder: (BuildContext context) {
                        return Naver();
                      }));
                    },
                  ),
                ],
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
              ),
            ],
          )
        ],
      ),
    );
  }
}

//Catbot/////////////////////////////////////////////////////////////////////////////////////////////////////////

class WebViewExample extends StatefulWidget {
  @override
  _WebViewExampleState createState() => _WebViewExampleState();
}

class _WebViewExampleState extends State<WebViewExample> {
  TextEditingController controller = TextEditingController();
  FlutterWebviewPlugin flutterWebviewPlugin = FlutterWebviewPlugin();
  var urlString =
      "http://121.67.246.252:5002/guest/conversations/production/322e875179d74d7a8c87f11099feea6f";

  launchUrl() {
    setState(() {
      urlString = controller.text;
      flutterWebviewPlugin.reloadUrl(urlString);
    });
  }

  @override
  void initState() {
    super.initState();
    flutterWebviewPlugin.onStateChanged.listen((WebViewStateChanged wvs) {
      print(wvs.type);
    });
  }

  @override
  Widget build(BuildContext context) {
    return WebviewScaffold(
      appBar: AppBar(
        title: TextField(
          autofocus: false,
          controller: controller,
          textInputAction: TextInputAction.go,
          onSubmitted: (url) => launchUrl(),
          style: TextStyle(color: Colors.white),
          decoration: InputDecoration(
            border: InputBorder.none,
            hintText: "Enter Url Here",
            hintStyle: TextStyle(color: Colors.white),
          ),
        ),
        actions: <Widget>[
          IconButton(
            icon: Icon(Icons.navigate_next),
            onPressed: () => launchUrl(),
          )
        ],
      ),
      url: urlString,
      withZoom: false,
    );
  }
}

//Alarm//////////////////////////////////////////////////////////////////////////////////////////////////////////

class Alarm extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        // dismiss the keyboard or focus
        FocusScopeNode currentFocus = FocusScope.of(context);
        if (!currentFocus.hasPrimaryFocus) {
          currentFocus.unfocus();
        }
      },
      child: MaterialApp(
        title: 'Medicine Reminder',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          primaryColor: Color(0xff42a5f5),
          accentColor: Color(0xff42a5f5),
        ),
        home: MyMedicineRemainder(),
      ),
    );
  }
}

class MyMedicineRemainder extends StatefulWidget {
  MyMedicineRemainder();

  @override
  _MyMedicineReminder createState() => _MyMedicineReminder();
}

class _MyMedicineReminder extends State<MyMedicineRemainder> {
  @override
  Widget build(BuildContext context) {
    final deviceHeight = MediaQuery.of(context).size.height;
    MedicineModel model;
    return ScopedModel<MedicineModel>(
      model: model = MedicineModel(),
      child: Scaffold(
          floatingActionButton: FloatingActionButton(
            onPressed: () {
              buildBottomSheet(deviceHeight, model);
            },
            child: Icon(
              Icons.add,
              size: 40,
              color: Colors.white,
            ),
            backgroundColor: Theme.of(context).accentColor,
          ),
          body: SafeArea(
            child: Column(
              children: <Widget>[
                MyAppBar(greenColor: Theme.of(context).primaryColor),
                Expanded(
                  child: ScopedModelDescendant<MedicineModel>(
                    builder: (context, child, model) {
                      return Stack(children: <Widget>[
                        buildMedicinesView(model),
                        (model.getCurrentIconState() == DeleteIconState.hide)
                            ? Container()
                            : DeleteIcon()
                      ]);
                    },
                  ),
                )
              ],
            ),
          )),
    );
  }

  FutureBuilder buildMedicinesView(model) {
    return FutureBuilder(
      future: model.getMedicineList(),
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          print(snapshot.data);
          if (snapshot.data.length == 0) {
            // No data
            return Center(child: MedicineEmptyState());
          }
          return MedicineGridView(snapshot.data);
        }
        return (Container());
      },
    );
  }

  void buildBottomSheet(double height, MedicineModel model) async {
    var medicineId = await showModalBottomSheet(
        shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.only(
                topLeft: Radius.circular(45), topRight: Radius.circular(45))),
        context: context,
        isScrollControlled: true,
        builder: (context) {
          return FadeAnimation(
            .6,
            AddMedicine(height, model.getDatabase(), model.notificationManager),
          );
        });

    if (medicineId != null) {
      Fluttertoast.showToast(
          msg: "알람이 추가됐습니다!",
          toastLength: Toast.LENGTH_SHORT,
          gravity: ToastGravity.BOTTOM,
          timeInSecForIos: 1,
          backgroundColor: Theme.of(context).accentColor,
          textColor: Colors.white,
          fontSize: 20.0);

      setState(() {});
    }
  }
}

//HowtoGo///////////////////////////////////////////////////////////////////////////////////////

class Naver extends StatefulWidget {
  @override
  _NaverState createState() => _NaverState();
}

class _NaverState extends State<Naver> {
  TextEditingController controller = TextEditingController();
  FlutterWebviewPlugin flutterWebviewPlugin = FlutterWebviewPlugin();
  var urlString =
      "https://www.google.co.kr/maps/dir//%EA%B2%BD%EA%B8%B0%EB%8F%84+%EA%B3%A0%EC%96%91%EC%8B%9C+%EC%9D%BC%EC%82%B0%EB%8F%99%EA%B5%AC+%EC%8B%9D%EC%82%AC%EB%8F%99+%EB%8F%99%EA%B5%AD%EB%A1%9C+27+%EB%8F%99%EA%B5%AD%EB%8C%80%ED%95%99%EA%B5%90+%EC%9D%BC%EC%82%B0%EB%B3%91%EC%9B%90/@37.6164829,126.8875215,11z/data=!4m7!4m6!1m1!4e2!1m2!1m1!1s0x357c9041b3bd5e29:0x1deb82639d70760a!3e3?hl=ko";
//"https://m.place.naver.com/attraction/list?query=%EA%B3%B5%EC%A0%81%EB%A7%88%EC%8A%A4%ED%81%AC&x=126.9973707&y=37.5652295&sessionId=cMlYy4CzoznrGxstdak6Sg%3D%3D&entry=ple&bounds=126.9796814%3B37.543862%3B127.01506%3B37.5865909";
  launchUrl() {
    setState(() {
      urlString = controller.text;
      flutterWebviewPlugin.reloadUrl(urlString);
    });
  }

  @override
  void initState() {
    super.initState();
    flutterWebviewPlugin.onStateChanged.listen((WebViewStateChanged wvs) {
      print(wvs.type);
    });
  }

  @override
  Widget build(BuildContext context) {
    return WebviewScaffold(
      url: urlString,
      withZoom: false,
    );
  }
}

//MediDic////////////////////////////////////////////////////////////////////////////////////////

class MediDic extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return InheritedManga(
      helper: Helper(),
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'MediDic',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: MyHomePage(title: 'MediDic'),
      ),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: NestedScrollView(
      headerSliverBuilder: (buildContext, headerSliverBuilder) {
        return <Widget>[
          SliverAppBar(
            floating: true,
            snap: true,
            title: Text('의학사전'),
            actions: <Widget>[
              IconButton(
                icon: Icon(Icons.search),
                onPressed: () {
                  showSearch(context: context, delegate: SearchManga());
                },
              )
            ],
          ),
        ];
      },
      body: FutureBuilder<List<Manga>>(
        initialData: List<Manga>(),
        future: InheritedManga.of(context).helper.getAllManga(),
        builder: (BuildContext context, AsyncSnapshot<List<Manga>> snapshot) {
          switch (snapshot.connectionState) {
            case ConnectionState.active:
            case ConnectionState.waiting:
              return Center(
                child: RefreshProgressIndicator(),
              );
            case ConnectionState.none:
              return Center(
                child: Text('Tidak ada koneksi'),
              );
            case ConnectionState.done:
              if (snapshot.hasError) {
                return Center(
                  child: Text('Data yang diterima salah'),
                );
              }
              return ListView.builder(
                itemCount: snapshot.data.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    leading: Icon(Icons.book),
                    title: Text(snapshot.data[index].title),
                    onTap: () async {
                      await Scaffold.of(context).showSnackBar((SnackBar(
                          content: Text("${snapshot.data[index].url}"))));
                    },
                  );
                },
              );
          }
          return Column();
        },
      ),
    ));
  }
}

// This is the theme of your applicationd
//
// Try running your application with "flutter run". You'll see the
// application has a blue toolbar. Then, without quitting the app, try
// changing the primarySwatch below to Colors.green and then invoke
// "hot reload" (press "r" in the console where you ran "flutter run",
// or simply save your changes to "hot reload" in a Flutter IDE).
// Notice that the counter didn't reset back to zero; the application
// is not restarted.
// This makes the visual density adapt to the platform that you run
// the app on. For desktop platforms, the controls will be smaller and
// closer together (more dense) than on mobile platforms.
