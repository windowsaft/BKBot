# :crown: BKBot

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


<script>
    const url = "https://meme-api.herokuapp.com/gimme/programmerhumor";

    fetch(url)
        .then((response) => {
        return response.json();
        })
        .then((data) => {
        //console.log(data["url"]);
        document.getElementById("meme").src=data["url"];
        });
</script>

<picture>
      <img alt="oop an error occured" id="meme">
</picture>