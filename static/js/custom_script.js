function filterCards(category) {
  var cards = document.querySelectorAll('.col');

  cards.forEach(function(card) {
    var cardCategory = card.getAttribute('data-category');

    if (category === 'all' || cardCategory === category) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}
