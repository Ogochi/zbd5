# ZBD 5

Michał Ołtarzewski - 382783

## Wymagania

 - **Docker**
 - **docker-compose**

albo

 - **Docker**
 - **Python3**

## Instrukcja uruchomienia

#### Szybki start

W głównym katalogu:
1. ``` docker-compose build ```
2. ``` docker-compose up ```

Kończymy poprzez: ``` docker-compose down ``` 

#### Wolniejsza alternatywa

W głównym katalogu:
1. ``` ./postup.sh ```
2. ``` ./init_exe.sh ``` - podajemy hasło `admin1`

Następnie w każdym z katalogów aplikacji z osobna:
1. ``` pip3 install -r requirements.txt ```
2. ``` python3 app.py ```

Kończymy całość poprzez: ``` ./postdown.sh ``` 

## Opis

Po wykonaniu instrukcji posiadamy postgres'a wraz z czterema serwisami:

 - `advert_display` - localhost:**5000** - "Zbieracz danych o wyświetleniach"
 - `advert_info` - localhost:**5001** - "Zbieracz danych o reklamach"
 - `user_info` - localhost:**5002** - "Zbieracz danych o internautach"
 - `all_stats` - localhost:**5003** - "Wyświetlacz sum"
 - `postgres` - localhost:**5432**

Każdy z programów posiada dokładnie jeden endpoint: `/graphql`. Przy jego użyciu jesteśmy w stanie używać każdego z serwisów. Jest to możliwe przy użyciu HTTP na dwa sposoby:
 - interfejs graficzny `GraphiQL` znajdujący się pod `GET`
 - normalna komunikacja z serwerem `GraphQL` znajdującym się pod `POST`

## Przykładowe operacje na serwisach

#### advert_display

```js
mutation {
  userSeenAdvert(advertDisplay: {
    userId: "01aa0956-1afc-4e97-9df6-487f95a190d6"
    advertId: "7fc99b4c-a51c-4f73-8362-a3d8c9638416"
    displayTime: "2006-01-02T16:04:05"
  }) {
    ok
  }
}
```

#### advert_info

```js
mutation {
  createAdverts(adverts: [
    {
      height: 12
      width: 22222
      mainColor: "#FFFFF"
      textContents: ["cyberpunk", "lol", "xxx"]
    },
    {
      height: 13
      width: 2
      mainColor: "#AAAAA"
    }
  ]) {
    ok
  }
}
```

#### user_info

```js
mutation {
  createUsers(users: [
    {
      gender: "M"
      yearlyIncome: 22222
      longitude: 61.22
      latitude: 15.1
      interests: ["cyberpunk", "lol"]
    }
  ]) {
    ok
  }
}
```

#### all_stats

```js
query {
  advertDisplays {
    edges {
      node {
        advertId
        userId
        displayTime
        advert {
          mainColor
        }
        user {
          yearlyIncome
        }
      }
    }
  }
}
```

```js
query {
  advertsCount(
    startDate: "2006-01-02T16:04:05",
    endDate: "2006-02-02T16:04:05")
}
```

## Podsumowanie

Nie udało mi się zaimplementować `Wyświetlacza Sum` tak, żeby do końca "Dla danego okresu i wybranych dowolnie parametrów mówi ile w tym czasie było wyświetleń reklam.". Mógłbym zaimplementować ręcznie każdy możliwy parametr zapytań, ale wydaje mi się, że nie o to chodziło. W tym miejscu niestety ograniczyła mnie wybrana technologia - Python + Flask + SqlAlchemy + Graphene. Gdybym zaczął robić projekt np w Django, to nie byłoby problemu. Tam bezpośrednio w modelu GraphQL można zdefiniować jakie pola mogą mieć jakie dokładnie rodzaje filtrów.