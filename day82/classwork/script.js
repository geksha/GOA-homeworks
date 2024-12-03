const objects = [
    {name: 'lasha', age: 16 },
    {name: 'gurami', age: 42 },
    {name: 'gega', age: 15 }
  ];
  
  for (let i in objects) {
    let currentObject = objects[i];
    for (let key in currentObject) {
      console.log(`${key}: ${currentObject[key]}`);
    }
  }
  
  for (let obj of objects) {
    for (let value of Object.values(obj)) {
      console.log(value);
    }
  }