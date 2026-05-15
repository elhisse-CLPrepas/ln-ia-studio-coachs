document.documentElement.classList.add("js-ready");

document.querySelectorAll("details").forEach((item) => {
  item.addEventListener("toggle", () => {
    if (!item.open) return;

    document.querySelectorAll("details").forEach((other) => {
      if (other !== item) other.removeAttribute("open");
    });
  });
});

const replaySection = document.querySelector("[data-replay-section]");

if (replaySection) {
  const form = replaySection.querySelector("[data-replay-form]");
  const emailInput = replaySection.querySelector("[data-replay-email]");
  const message = replaySection.querySelector("[data-replay-message]");
  const player = replaySection.querySelector("[data-replay-player]");
  const lock = replaySection.querySelector("[data-replay-lock]");
  const video = replaySection.querySelector("[data-replay-video]");
  const storageKey = "lnIaReplayEmail";
  const storage = {
    get() {
      try {
        return localStorage.getItem(storageKey);
      } catch {
        return "";
      }
    },
    set(email) {
      try {
        localStorage.setItem(storageKey, email);
      } catch {
        // The replay still unlocks when browser storage is unavailable.
      }
    },
  };

  const unlockReplay = (email) => {
    if (email) storage.set(email);
    player.removeAttribute("aria-hidden");
    lock.hidden = true;
    video.hidden = false;
    message.textContent = "Replay activé. Vous pouvez regarder ou télécharger la vidéo.";
  };

  const savedEmail = storage.get();
  const isIos =
    /iPad|iPhone|iPod/.test(navigator.userAgent) ||
    (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  if (savedEmail) {
    emailInput.value = savedEmail;
    unlockReplay(savedEmail);
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    if (!emailInput.checkValidity()) {
      message.textContent = "Veuillez entrer une adresse email valide.";
      emailInput.focus();
      return;
    }

    unlockReplay(emailInput.value.trim());
    if (isIos) {
      message.textContent =
        "Replay activé. Sur iPhone, utilisez le bouton Google Drive puis l'option Partager ou Télécharger.";
    }
  });
}
