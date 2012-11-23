/* sortedset.vala
 *
 * Copyright (C) 2009  Didier Villevalois, Maciej Piechotka
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.

 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.

 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
 *
 * Author:
 * 	Maciej Piechotka <uzytkownik2@gmail.com>
 */

/**
 * A sorted set, which you can navigate over and get sub-sets of.
 */
public interface Gee.SortedSet<G> : Gee.Set<G> {
	/**
	 * Returns the first element of the sorted set. Set must not be empty.
	 *
	 * @return the first element in the sorted set
	 */
	public abstract G first ();

	/**
	 * Returns the last element of the sorted set. Set must not be empty.
	 *
	 * @return the last element in the sorted set
	 */
	public abstract G last ();

	/**
	 * Returns a {@link BidirIterator} that can be used for bi-directional
	 * iteration over this sorted set.
	 *
	 * @return a {@link BidirIterator} over this sorted set
	 */
	public abstract BidirIterator<G> bidir_iterator ();

	/**
	 * Returns a {@link BidirIterator} initialy pointed at the specified
	 * element.
	 *
	 * @param element the element to point the iterator at
	 *
	 * @return        a {@link BidirIterator} over this sorted set, or null if
	 *                the specified element is not in this set
	 */
	public abstract BidirIterator<G>? iterator_at (G element);

	/**
	 * Returns the element which is strictly lower than the specified element.
	 *
	 * @param element the element which you want the lower element for
	 *
	 * @return        the corresponding element
	 */
	public abstract G? lower (G element);

	/**
	 * Returns the element which is strictly higher than the specified element.
	 *
	 * @param element the element which you want the strictly higher element
	 *                for
	 *
	 * @return        the corresponding element
	 */
	public abstract G? higher (G element);

	/**
	 * Returns the element which is lower or equal then the specified element.
	 *
	 * @param element the element which you want the lower or equal element for
	 *
	 * @return        the corresponding element
	 */
	public abstract G? floor (G element);

	/**
	 * Returns the element which is higher or equal then the specified element.
	 *
	 * @param element the element which you want the higher or equal element
	 *                for
	 *
	 * @return        the corresponding element
	 */
	public abstract G? ceil (G element);

	/**
	 * Returns the sub-set of this sorted set containing elements strictly
	 * lower than the specified element.
	 *
	 * @param before the lower inclusive bound for the sub-set
	 *
	 * @return     the corresponding sub-set of this sorted set
	 */
	public abstract SortedSet<G> head_set (G before);

	/**
	 * Returns the sub-set of this sorted set containing elements equal or
	 * higher than the specified element.
	 *
	 * @param after the higher exclusive bound for the sub-set
	 *
	 * @return   the corresponding sub-set of this sorted set
	 */
	public abstract SortedSet<G> tail_set (G after);

	/**
	 * Returns the right-open sub-set of this sorted set, thus containing
	 * elements equal or higher than the specified ``from`` element, and stricly
	 * lower than the specified ``to`` element.
	 *
	 * @param from the lower inclusive bound for the sub-set
	 * @param to   the higher exclusive bound for the sub-set
	 *
	 * @return     the corresponding sub-set of this sorted set
	 */
	public abstract SortedSet<G> sub_set (G from, G to);
}
