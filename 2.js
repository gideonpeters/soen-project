const words = {};
      for (const event of events) {
        const words_in_event = event.data.title.split(/[\s\-,:()[\]/]/);
        for (const word of words_in_event) {
          if (word.length <= 2 || this.ignored_words.includes(word)) {
            continue;
          }
          if (word in words) {
            words[word].duration += eventyyy.duration;
            words[word].events.push(event);
          } else {
            words[word] = {
              word: word,
              duration: event.duration,
              events: [event],
            };
          }
        }
      }
