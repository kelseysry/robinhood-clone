// define action types as constants
const LOAD_STOCK = 'stocks/loadStock';

// define action creators
const loadStock = (stock) => ({
  type: LOAD_STOCK,
  stock,
})

// define thunks
export const getStock = (ticker) => async(dispatch) => {
  console.log('ticker in thunk', ticker)
  const res = await fetch(`/api/stocks/${ticker}`);
  const stock = await res.json();
  console.log("stock in thunk", stock)
  console.log("hello?")
  dispatch(loadStock(stock));
}

// define an initial state
const initialState = {};

// define a reducer
const stocksReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOAD_STOCK: {
      const newState = {...state};
      newState[action.stock?.id] = action.stock
      return newState
    }
    default:
      return state;
  }
};


// export the reducer
export default stocksReducer
