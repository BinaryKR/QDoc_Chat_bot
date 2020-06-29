import 'package:http/http.dart';
import 'package:html/dom.dart';
import 'package:html/parser.dart';

import 'manga.dart';
var uurl = "http://www.snuh.org/health/encyclo";
class Helper {
  Client _client;
  List<Manga> _manga = [];

  Helper() {
    this._client = Client();
  }

  Future<List<Manga>> getAllManga() async {
    if (_manga.length != 0) return _manga;
    final response = await _client.get(
        'http://www.snuh.org/health/encyclo/search.do?searchKey=S&searchWord=가');
    final document = parse(response.body);
    final mangasPerTitle = document.getElementsByClassName('boxInner');
    for (Element mangaPerTitle in mangasPerTitle) {
      final mangas = mangaPerTitle.getElementsByTagName('li');
      for (Element m in mangas) {
        final aTag = m.getElementsByTagName('a')[0];
        final title = aTag.text;
        final url1 = aTag.attributes['href'];
        final url2 = url1.replaceAll("\n", "");
        final url3 = url2.replaceAll("\t", "");
        final url4 = url3.replaceAll(".", "");
        final url5 = url4.replaceAll("do", ".do");
        final url = uurl+url5;
        final response2 = await _client.get(url);
        final document2 = parse(response2.body);
        final mangasPerTitle2 = document2.getElementsByClassName('encView')[0];
        final docu = mangasPerTitle2.text;
        //print(mangasPerTitle2.text);
        final manga = Manga(title: title, url: docu);
//        print('------------aTag-----------');
//        print(aTag);
//        print('------------title-----------');
//        print(title);
//        print('------------url-----------');
//        print(url);
//        print('------------aTag-----------');
//        print(manga);
        _manga.add(manga);
      }
    }
    return _manga;
  }

  Future<List<Manga>> getMangaByQuery(String query) async {
    if (_manga.length == 0) await getAllManga();
    if (query == null || query?.isEmpty) return _manga;
    return _manga
        .where(
            (manga) => manga.title.toLowerCase().contains(query.toLowerCase()))
        .toList();
  }
}
