import { useEffect } from 'react';

import { useDispatch, useSelector } from 'react-redux';


import {useParams} from 'react-router-dom';

// dispatch - so we can send request to the deux store
// dispatch a thunk to fetch the info and render the info
// from the redux store in a component

// import the thunk creator
import { getStock } from '../../store/stocks';

function SingleStockPage() {
  const dispatch = useDispatch();
  const stockObj = useSelector((state) => state.stocks);
  const stock = Object.values(stockObj)
  const { ticker } = useParams();
  console.log("ticker", ticker)

  useEffect(() => {
    dispatch(getStock(ticker));
  }, [dispatch])

  console.log("stock obj", stock)
  return (
    <>
    <div>  stock name: {stock[0]?.name} </div>
    <div>  stock about: {stock[0]?.about} </div>
    <div>  stock ceo: {stock[0]?.ceo} </div>
    {/* <div>  stock ceo: {stock[0].stock.ceo} </div> */}
    </>
  )
}


export default SingleStockPage
